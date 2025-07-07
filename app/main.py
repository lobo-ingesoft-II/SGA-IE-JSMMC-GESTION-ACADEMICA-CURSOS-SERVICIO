from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import cursos

from app.backend.session import Base, engine


# Librerias para Observabilidad
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.responses import Response
from app.routers.cursos import REQUEST_COUNT_COURSES_ROUTERS, REQUEST_LATENCY_COURSES_ROUTERS, ERROR_COUNT_COURSES_ROUTERS


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


# Middleware para observabilidad
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        status = response.status_code
    except Exception as e:
        status = 500
        raise e
    finally:
        latency = time.time() - start_time
        endpoint = request.url.path
        method = request.method

        REQUEST_COUNT_COURSES_ROUTERS.labels(endpoint=endpoint, method=method).inc()
        REQUEST_LATENCY_COURSES_ROUTERS.labels(endpoint=endpoint, method=method).observe(latency)


        
        if status >= 400:
            ERROR_COUNT_COURSES_ROUTERS.labels(endpoint=endpoint, method=method, status_code=str(status)).inc()

    return response

# Registrar rutas
app.include_router(cursos.router, prefix="/cursos", tags=["Cursos"])
