# Servicio de Cursos

## Descripción
Este servicio permite gestionar los cursos en el sistema académico. Proporciona funcionalidades para crear, obtener y listar cursos, facilitando su integración con otros módulos.

## Endpoints

## Tabla de Endpoints

| Método | Endpoint                                         | Descripción                              | Request Body         | Respuesta Principal                |
|--------|--------------------------------------------------|------------------------------------------|----------------------|------------------------------------|
| POST   | `/cursos/`                                       | Registrar un curso                       | Sí                   | Curso creado (200 OK)              |
| GET    | `/cursos/{id_curso}`                             | Obtener un curso por ID                   | No                   | Curso o 404 Not Found              |
| GET    | `/cursos/`                                       | Listar todos los cursos                   | No                   | Lista de cursos                    |
| GET    | `/cursos/profesores/{id_profesor}/cursos`        | Listar cursos por profesor                | No                   | Lista de cursos o 404 Not Found    |
| DELETE | `/cursos/{id_curso}`                             | Eliminar un curso por ID                  | No                   | Curso eliminado o 404 Not Found    |
| PUT    | `/cursos/{id_curso}/profesor/{id_profesor}`      | Actualizar director de un curso           | No                   | Curso actualizado o 404 Not Found  |

## Instalación

1. Asegúrate de tener el entorno configurado:

   ```bash
   pip install -r requirements.txt
   ```
2. Configura la base de datos en el archivo `.env`:

   ```env
   DATABASE_URL="mysql+pymysql://user:password@host:port/database"
   ```
3. Ejecuta el servidor:

   ```bash
   uvicorn app.main:app --reload --port 8004
   ```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest app/tests/test_cursos.py
```

## Dependencias

* **FastAPI**: Framework principal.
* **SQLAlchemy**: ORM para manejar la base de datos.
* **Pytest**: Framework para pruebas unitarias.

## Documentación interactiva

Accede a la documentación Swagger en [http://localhost:8004/docs](http://localhost:8004/docs) o ReDoc en [http://localhost:8004/redoc](http://localhost:8004/redoc).

## Contacto

Para más información, contactar con el equipo de desarrollo.
