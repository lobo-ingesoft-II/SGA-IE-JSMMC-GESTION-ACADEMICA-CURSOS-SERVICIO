from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.cursos import CursoCreate, CursoResponse
from app.services.cursos import create_curso, get_curso, list_cursos
from app.db import SessionLocal
from app.services.cursos import list_cursos_by_profesor



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CursoResponse)
def create(curso: CursoCreate, db: Session = Depends(get_db)):
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
def get_cursos_de_profesor(id_profesor: int, db: Session = Depends(get_db)):
    return list_cursos_by_profesor(db, id_profesor)
