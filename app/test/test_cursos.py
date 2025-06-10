from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_curso():
    response = client.post("/cursos/", json={
        "nombre": "Curso 101",
        "grado": "Primero",
        "anio_lectivo": 2025,
        "id_sede": 1,
        "director_profesor": 1
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "Curso 101"

def test_get_curso():
    response = client.get("/cursos/1")
    assert response.status_code == 200
    assert "nombre" in response.json()

def test_list_cursos():
    response = client.get("/cursos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)