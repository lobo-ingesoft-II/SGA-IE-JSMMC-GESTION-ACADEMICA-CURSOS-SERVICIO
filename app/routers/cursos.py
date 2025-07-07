from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.cursos import CursoCreate, CursoResponse
from app.services.cursos import create_curso, get_curso, list_cursos, delete_curso, update_in_curso_professorId
from app.backend.session import SessionLocal
from app.services.cursos import list_cursos_by_profesor
from app.backend.database import get_db



# Librerias para Observabilidad
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response
from prometheus_client import CollectorRegistry, generate_latest


router = APIRouter()

# Metricas 
REQUEST_COUNT_COURSES_ROUTERS = Counter(
    "http_requests_total", 
    "TOTAL PETICIONES HTTP router-cursos",
    ["method", "endpoint"]
)

REQUEST_LATENCY_COURSES_ROUTERS = Histogram(
    "http_request_duration_seconds", 
    "DURACION DE LAS PETICIONES router-cursos",
    ["method", "endpoint"],
    buckets=[0.1, 0.3, 1.0, 2.5, 5.0, 10.0]  
)

# 3. Errores por endpoint
ERROR_COUNT_COURSES_ROUTERS = Counter(
    "http_request_errors_total",
    "TOTAL ERRORES HTTP (status >= 400)",
    ["endpoint", "method", "status_code"]
)

# Ruta para observabilidad 
@router.get("/custom_metrics")
def custom_metrics():
    registry = CollectorRegistry()
    registry.register(REQUEST_COUNT_COURSES_ROUTERS)
    registry.register(REQUEST_LATENCY_COURSES_ROUTERS)
    registry.register(ERROR_COUNT_COURSES_ROUTERS)
    return Response(generate_latest(registry), media_type=CONTENT_TYPE_LATEST)




@router.post("/", response_model=CursoResponse)
def create(curso: CursoCreate, db: Session = Depends(get_db)):
    curso = create_curso(db, curso)
    return create_curso(db, curso)

@router.get("/{id_curso}", response_model=CursoResponse)
def get(id_curso: int, db: Session = Depends(get_db)):
    db_curso = get_curso(db, id_curso)
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso not found")
    return db_curso

@router.get("/", response_model=list[CursoResponse])
def list_all(db: Session = Depends(get_db)):
    return list_cursos(db)

@router.get("/profesores/{id_profesor}/cursos", response_model=list[CursoResponse])
async def get_cursos_de_profesor(id_profesor: int, db: Session = Depends(get_db)):
    cursos = list_cursos_by_profesor(db, id_profesor)
    if cursos is None: 
        raise  HTTPException(status_code=404, detail="Profesor no encontrado")
    return cursos

@router.delete("/{id_curso}", response_model=CursoResponse)
async def delete(id_curso: int, db: Session = Depends(get_db)):
    curso = delete_curso(db, id_curso)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    return curso

@router.put("/{id_curso}/profesor/{id_profesor}", response_model=CursoResponse)
async def update_profesor_in_curso(id_curso: int, id_profesor: int, db: Session = Depends(get_db)):
    curso = update_in_curso_professorId(db, id_profesor, id_curso)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso or Profesor not found")
    return curso