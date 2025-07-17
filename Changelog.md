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

## [1.0.2] - 2025-06-10
### Corregido
- Se corrige FK del modelo
### Agregado
- Se agrega el puerto 8004 al README.md
- Se agrega sección de documentación interactiva

## [1.0.3] - 2025-07-16
### Agregado
- Prueba unitaria para verificar el manejo de errores al solicitar un curso inexistente.
- Configuración de la base de datos SQLite temporal para pruebas.
- Ajustes en las pruebas unitarias para garantizar el uso de SQLite.

### Corregido
- Importación de `patch` y `Mock` en las pruebas unitarias.
- Importación de la clase `Curso` en las pruebas unitarias.
- Resolución de problemas con `Base.metadata.create_all` en las pruebas.W