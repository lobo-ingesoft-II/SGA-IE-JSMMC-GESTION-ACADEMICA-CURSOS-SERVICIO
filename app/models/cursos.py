from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base

class Curso(Base):
    __tablename__ = "cursos"

    id_curso = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    grado = Column(String(20), nullable=False)
    anio_lectivo = Column(Integer, nullable=False)
    id_sede = Column(Integer, nullable=False)
    director_profesor = Column(Integer, nullable=False)