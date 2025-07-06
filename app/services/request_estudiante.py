import requests # Para hacer solicitudes HTTP 
from app.backend.config import settings

# FUNCIÓN PARA OBTENER JSON DESDE LA API(PRE-MATRICULA)
def obtener_profesor(id: str):
    # Crear la URL del servidor de la API de pre-registro 
    url_servidor = settings.url_api_sga_autenticacion

    # **GET** `/estudiantes/{id_estudiante}`
    url = url_servidor + f"/profesor/{id}"  
  
    # Realizar la solicitud GET a la API 
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    
    if response.status_code == 200:
        data = response.json()  # Obtener los datos en formato JSON
        # print(data)

        if isinstance(data, dict) and data:  # Si es un diccionario y no está vacío
            return data  # Retorna el objeto completo del profesor
        else:
            return None        
    else:
        return None