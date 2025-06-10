# Changelog - Servicio de Cursos

## [1.0.0] - 2025-06-09
### Agregado
- Creación del servicio de cursos.
- Endpoint **POST** `/cursos/` para registrar un nuevo curso.
- Endpoint **GET** `/cursos/{id_curso}` para obtener un curso por ID.
- Endpoint **GET** `/cursos/` para listar todos los cursos.
- Integración de modelos, esquemas y servicios con SQLAlchemy y Pydantic.
- Pruebas unitarias básicas para las operaciones CRUD de cursos.

## [1.0.1] - 2025-06-09
### Corregido
- Validación de longitud mínima y máxima para el nombre del curso.
- Mejora en los mensajes de error para registros no encontrados.
- Se ajusta titulo en el README.md