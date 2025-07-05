from sqlalchemy.orm import Session
from app.models.cursos import Curso
from app.schemas.cursos import CursoCreate
from app.services.request_estudiante import obtener_profesor
# from app.models.profesor_curso import profesor_curso

def create_curso(db: Session, curso: CursoCreate):
    db_curso = Curso(**curso.model_dump())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

def get_curso(db: Session, id_curso: int):
    
    db_curso = db.query(Curso).filter(Curso.id_curso == id_curso).first()
    return db_curso


def delete_curso(db: Session, id_curso: int):
    curso = db.query(Curso).filter(Curso.id_curso == id_curso).first()
    if curso:
        db.delete(curso)
        db.commit()
        return curso
    return None

def list_cursos(db: Session):
    return db.query(Curso).all()

def update_in_curso_professorId(db: Session, id_profesor: int, id_curso: int):

    # Obtener el profesor de la API profesor y con eso revisar si existe 
    profesorDic = obtener_profesor(id_profesor)
    print(profesorDic)
    if not profesorDic:
        return None

    # Verificar si el curso existe
    # print("id Curso",id_curso)
    curso = db.query(Curso).filter(Curso.id_curso == id_curso).first()
    # print(curso)

    if not curso:
        return None

    # Actualizar el director por el id del profesor 
    curso.director_profesor = id_profesor
    db.commit()
    db.refresh(curso)

    return curso


def list_cursos_by_profesor(db: Session, profesor_id: int):

    # Obtener el profesor de la API profesor y con eso verificar si existe 
    profesorDic = obtener_profesor(profesor_id)
    if not profesorDic:
        return None

    # Buscar todos los cursos que estén asociados al profesor
    cursos = db.query(Curso).filter(Curso.director_profesor == profesor_id).all()

    # Retornar la lista (vacía si no hay cursos)
    return cursos

    # return (
    #     db.query(Curso)
    #     .join(profesor_curso, Curso.id_curso == profesor_curso.c.id_curso)
    #     .filter(profesor_curso.c.id_profesor == profesor_id)
    #     .all()
    # )