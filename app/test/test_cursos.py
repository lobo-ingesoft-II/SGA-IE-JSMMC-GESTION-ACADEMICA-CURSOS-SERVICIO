from fastapi.testclient import TestClient
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.backend.session import Base
from app.routers.cursos import get_db
from sqlalchemy.sql import text
from unittest.mock import patch, Mock
from app.models.cursos import Curso

# Set DATABASE_URL environment variable for tests
os.environ["DATABASE_URL"] = "sqlite:///./test_temp_cursos.db"

from app.main import app

# Configure temporary SQLite database for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp_cursos.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def limpiar_tablas():
    db = TestingSessionLocal()
    db.execute(text("DELETE FROM cursos"))
    db.commit()
    db.close()

@patch("requests.get")
def test_create_curso(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    response = client.post("/cursos/", json={
        "nombre": "Curso 101",
        "grado": "Primero",
        "anio_lectivo": 2025,
        "id_sede": 1,
        "director_profesor": 1
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "Curso 101"

@patch("requests.get")
def test_get_curso(mock_get):
    db = TestingSessionLocal()
    curso = Curso(id_curso=1, nombre="Curso 101", grado="Primero", anio_lectivo=2025, id_sede=1, director_profesor=1)
    db.add(curso)
    db.commit()
    db.close()

    response = client.get("/cursos/1")
    assert response.status_code == 200
    assert "nombre" in response.json()

@patch("requests.get")
def test_get_nonexistent_curso(mock_get):
    response = client.get("/cursos/999")  # ID de curso que no existe
    assert response.status_code == 404
    assert response.json()["detail"] == "Curso not found"

@patch("requests.get")
def test_list_cursos(mock_get):
    db = TestingSessionLocal()
    curso = Curso(id_curso=1, nombre="Curso 101", grado="Primero", anio_lectivo=2025, id_sede=1, director_profesor=1)
    db.add(curso)
    db.commit()
    db.close()

    response = client.get("/cursos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Clean up the temporary database after tests
def teardown_module(module):
    try:
        os.remove("./test_temp_cursos.db")
    except FileNotFoundError:
        pass