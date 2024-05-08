# conexion.py
import pymongo
import ssl

# Define una función llamada "conectar_base_datos" que se utilizará para establecer una conexión a la base de datos.
def conectar_base_datos():
    # Define el nombre de usuario y contraseña para la conexión.
    usuario = "user"
    contraseña = "password_USER"

    # Crea una instancia del cliente de MongoDB utilizando pymongo.MongoClient().
    # Se especifica la URL de conexión, que incluye el nombre de usuario y contraseña, y el puerto donde se ejecuta MongoDB (localhost:27017).
    # Además, se habilita SSL y se desactiva la verificación del certificado utilizando "tlsAllowInvalidCertificates=True".
    cliente = pymongo.MongoClient(
        f"mongodb://{usuario}:{contraseña}@localhost:27017/",
        ssl=True,
        tlsAllowInvalidCertificates=True  # Desactiva la verificación del certificado
    )

    # Selecciona la base de datos "3v4_password" a la que se conectará el cliente.
    db = cliente["3v4_password"]

    # Selecciona la colección "usuarios" dentro de la base de datos.
    usuarios = db["usuarios"]

    # Devuelve la colección "usuarios" para que se pueda usar en otras partes del código.
    return usuarios
