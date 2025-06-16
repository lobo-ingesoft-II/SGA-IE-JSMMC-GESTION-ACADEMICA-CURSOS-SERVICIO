from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db import Base  # Asegúrate de que apunte a tu declarative base

profesor_curso = Table(
    "profesor_curso",
    Base.metadata,
    Column("id_profesor", Integer, ForeignKey("usuarios.id_usuario"), primary_key=True),
    Column("id_curso", Integer, ForeignKey("cursos.id_curso"), primary_key=True),
)
