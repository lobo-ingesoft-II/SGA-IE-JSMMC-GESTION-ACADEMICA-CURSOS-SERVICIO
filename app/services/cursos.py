from sqlalchemy.orm import Session
from app.models.cursos import Curso
from app.schemas.cursos import CursoCreate

def create_curso(db: Session, curso: CursoCreate):
    db_curso = Curso(**curso.dict())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

def get_curso(db: Session, id_curso: int):
    return db.query(Curso).filter(Curso.id_curso == id_curso).first()

def list_cursos(db: Session):
    return db.query(Curso).all()