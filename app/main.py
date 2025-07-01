from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import cursos

from app.backend.session import Base, engine

#Lee todas las clases que heredan de Base.
# Genera el SQL necesario para crear las tablas en la base de datos.
# No borra ni modifica tablas existentes, solo crea las que faltan.
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Cursos API")

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza con ["http://localhost:3000"] si deseas restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Registrar rutas
app.include_router(cursos.router, prefix="/cursos", tags=["Cursos"])
