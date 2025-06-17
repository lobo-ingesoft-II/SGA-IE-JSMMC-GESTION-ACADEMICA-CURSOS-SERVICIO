from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db import Base

curso_asignatura = Table(
    "curso_asignatura",
    Base.metadata,
    Column("id_curso", Integer, ForeignKey("cursos.id_curso"), primary_key=True),
    Column("id_asignatura", Integer, nullable=False),  # ID de asignatura del otro servicio
)