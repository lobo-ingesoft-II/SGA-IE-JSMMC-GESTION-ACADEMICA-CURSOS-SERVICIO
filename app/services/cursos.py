from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.cursos import Curso
from app.schemas.cursos import CursoCreate
from app.models.profesor_curso import profesor_curso
from app.models.curso_asignatura import curso_asignatura

def create_curso(db: Session, curso: CursoCreate):
    db_curso = Curso(
        nombre=curso.nombre,
        grado=curso.grado,
        anio_lectivo=curso.anio_lectivo,
        id_sede=curso.id_sede,
        director_profesor=curso.director_profesor,
    )
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)

    if curso.asignaturas:
        for id_asignatura in curso.asignaturas:
            db.execute(
                curso_asignatura.insert().values(
                    id_curso=db_curso.id_curso,
                    id_asignatura=id_asignatura
                )
            )
        db.commit()

    return db_curso

def get_curso(db: Session, id_curso: int):
    curso = db.query(Curso).filter(Curso.id_curso == id_curso).first()
    if not curso:
        return None
    # Obtener asignaturas asociadas
    asignaturas = db.execute(
        select(curso_asignatura.c.id_asignatura).where(curso_asignatura.c.id_curso == id_curso)
    ).scalars().all()
    curso.asignaturas = asignaturas
    return curso

def list_cursos(db: Session):
    cursos = db.query(Curso).all()
    for curso in cursos:
        asignaturas = db.execute(
            select(curso_asignatura.c.id_asignatura).where(curso_asignatura.c.id_curso == curso.id_curso)
        ).scalars().all()
        curso.asignaturas = asignaturas
    return cursos

def list_cursos_by_profesor(db: Session, id_profesor: int):
    cursos = db.query(Curso).filter(Curso.director_profesor == id_profesor).all()
    for curso in cursos:
        asignaturas = db.execute(
            select(curso_asignatura.c.id_asignatura).where(curso_asignatura.c.id_curso == curso.id_curso)
        ).scalars().all()
        curso.asignaturas = asignaturas
    return cursos