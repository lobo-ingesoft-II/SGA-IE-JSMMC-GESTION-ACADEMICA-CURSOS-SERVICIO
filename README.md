# Servicio de Cursos

## Descripción
Este servicio permite gestionar los cursos en el sistema académico. Proporciona funcionalidades para crear, obtener y listar cursos, facilitando su integración con otros módulos.

## Endpoints

### Registrar un curso
**POST** `/cursos/`

#### Request Body

```json
{
 "nombre": "Curso 101",
  "grado": "Primero",
  "anio_lectivo": 2025,
  "id_sede": 1,
  "director_profesor": 1,
  "asignaturas": [10, 11, 12]
}
```

#### Response

**Status:** 200 OK

```json
{
  "id_curso": 1,
  "nombre": "Curso 101",
  "grado": "Primero",
  "anio_lectivo": 2025,
  "id_sede": 1,
  "director_profesor": 1,
  "asignaturas": [10, 11, 12]
}
```

### Obtener un curso por ID

**GET** `/cursos/{id_curso}`

#### Response

**Status:** 200 OK

```json
{
  "id_curso": 1,
  "nombre": "Curso 101",
  "grado": "Primero",
  "anio_lectivo": 2025,
  "id_sede": 1,
  "director_profesor": 1,
  "asignaturas": [10, 11, 12]
}
```

**Status:** 404 Not Found

```json
{
  "detail": "Curso not found"
}
```

### Listar todas los cursos

**GET** `/cursos/`

#### Response

**Status:** 200 OK

```json
[
  {
    "id_curso": 1,
    "nombre": "Curso 101",
    "grado": "Primero",
    "anio_lectivo": 2025,
    "id_sede": 1,
    "director_profesor": 1,
    "asignaturas": [10, 11, 12]
  },
  {
    "id_curso": 2,
    "nombre": "Curso 102",
    "grado": "Segundo",
    "anio_lectivo": 2025,
    "id_sede": 1,
    "director_profesor": 2,
    "asignaturas": [13, 14]
  }
]
```

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
