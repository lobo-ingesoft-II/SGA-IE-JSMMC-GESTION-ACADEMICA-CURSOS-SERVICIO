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
  "director_profesor": 1
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
  "director_profesor": 1
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
  "director_profesor": 1
}
```

**Status:** 404 Not Found

```json
{
  "detail": "Curso not found"
}
```

### Listar todas las calificaciones

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
    "director_profesor": 1
  },
  {
    "id_curso": 2,
    "nombre": "Curso 102",
    "grado": "Segundo",
    "anio_lectivo": 2025,
    "id_sede": 1,
    "director_profesor": 2
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
   uvicorn app.main:app --reload
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

## Contacto

Para más información, contactar con el equipo de desarrollo.
