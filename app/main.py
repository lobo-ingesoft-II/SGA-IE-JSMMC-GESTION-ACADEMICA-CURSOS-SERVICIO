from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import cursos
from app.db import init_db, test_connection

app = FastAPI(title="Cursos API")

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza con ["http://localhost:3000"] si deseas restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

# Registrar rutas
app.include_router(cursos.router, prefix="/cursos", tags=["Cursos"])
