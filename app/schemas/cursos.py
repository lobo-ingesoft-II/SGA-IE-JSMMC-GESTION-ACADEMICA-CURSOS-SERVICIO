from pydantic import BaseModel
from typing import List

class CursoBase(BaseModel):
    nombre: str
    grado: str
    anio_lectivo: int
    id_sede: int
    director_profesor: int

class CursoCreate(CursoBase):
    asignaturas: List[int] = []

class CursoResponse(CursoBase):
    id_curso: int
    asignaturas: List[int] = []

    class Config:
        orm_mode = True