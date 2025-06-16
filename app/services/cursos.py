from sqlalchemy.orm import Session
from app.models.cursos import Curso
from app.schemas.cursos import CursoCreate
from app.models.profesor_curso import profesor_curso

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

def list_cursos_by_profesor(db: Session, profesor_id: int):
    return (
        db.query(Curso)
        .join(profesor_curso, Curso.id_curso == profesor_curso.c.id_curso)
        .filter(profesor_curso.c.id_profesor == profesor_id)
        .all()
    )