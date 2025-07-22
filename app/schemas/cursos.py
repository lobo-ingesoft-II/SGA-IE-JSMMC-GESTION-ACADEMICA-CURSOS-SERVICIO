from pydantic import BaseModel, ConfigDict

class CursoBase(BaseModel):
    nombre: str
    grado: str
    anio_lectivo: int
    id_sede: int
    director_profesor: int

class CursoCreate(CursoBase):
    pass

class CursoResponse(CursoBase):
    id_curso: int

    model_config = ConfigDict(from_attributes=True)