from app.backend.config import settings # Traer el valor de configuración de la URI de MongoDB
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError



# Configuración de la conexión remota
config = {
    'host': settings.host_mysql,
    'user': settings.user_mysql,
    'password': settings.password_mysql,
    'database': settings.database_mysql,
    'port': settings.port_mysql
}

print(config)
# Construir la URL de conexión




# Crear engine
engine = create_engine(settings.sqlalchemy_database_uri) # Gestiona las conexion en la app

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Crea una sección personalizada cada vez que la base de datos necesita realziar una operacion de CONSULTA, INSERTAR, ACTUALIZAR

# Base declarativa para modelos
Base = declarative_base()  # Es la clase base de la que SE DEBEN HEREDAR todos los modelos o tablas 


