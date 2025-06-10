from fastapi import FastAPI
from app.routers import cursos
from app.db import init_db, test_connection

app = FastAPI(title="Cursos API")

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

# Registrar rutas
app.include_router(cursos.router, prefix="/cursos", tags=["Cursos"])