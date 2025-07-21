import requests
from sqlalchemy.orm import Session
from app.models.cursos import Curso
from app.schemas.cursos import CursoCreate

API_SEDES_URL = "http://127.0.0.1:8000/sedes"
# REVISAR
# API_PROFESORES_URL = "http://127.0.0.1:8000/profesor"

def sede_existe(id_sede: int) -> bool:
    resp = requests.get(f"{API_SEDES_URL}/{id_sede}")
    return resp.status_code == 200

def profesor_existe(id_profesor: int) -> bool:
    resp = requests.get(f"{API_PROFESORES_URL}/{id_profesor}")
    return resp.status_code == 200

def create_curso(db: Session, curso: CursoCreate):
    # Validar sede
    if not sede_existe(curso.id_sede):
        raise ValueError("La sede no existe")
    # Validar profesor
    if not profesor_existe(curso.director_profesor):
        raise ValueError("El profesor no existe")
    db_curso = Curso(**curso.dict())
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