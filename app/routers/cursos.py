from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.cursos import CursoCreate, CursoResponse
from app.services.cursos import create_curso, get_curso, list_cursos, delete_curso, update_in_curso_professorId
from app.backend.session import SessionLocal
from app.services.cursos import list_cursos_by_profesor
from app.backend.database import get_db



router = APIRouter()



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