#login
from termcolor import cprint
from pyfiglet import figlet_format
from getpass import getpass
import time, os

def generate_login():
    selected_color = "green"
    header_text = "Login"
    header = figlet_format(header_text)
    cprint(header, color=selected_color)

def iniciar_sesion(usuarios):
    usuario_actual = None

    while True:
        if usuario_actual:
            print(f"¡Ya has iniciado sesión como {usuario_actual}!")
            print("1. Volver atrás.")
        else:
            generate_login()
            print("1. Login")
            print("2. Volver atrás")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1" and not usuario_actual:
            os.system("clear")
            generate_login()
            usuario = input("Ingrese su nombre de usuario: ")
            contraseña = getpass("Ingrese su contraseña: ")
            usuario_encontrado = usuarios.find_one({"usuario": usuario, "contraseña": contraseña})

            if usuario_encontrado:
                print("\033[92m\nInicio de sesión exitoso\033[0m")
                time.sleep(1)
                return usuario
            else:
                print("\033[91m\nNombre de usuario o contraseña incorrectos. Inténtelo nuevamente.\033[0m")
                time.sleep(2)
                os.system("clear")
        elif opcion == "2" or (opcion == "1" and usuario_actual):
            print("\033[92m\nVolviendo al menú principal.\033[0m")
            time.sleep(2)
            os.system("clear")
            return None  # Devolver None para indicar que el usuario eligió volver atrás
        else:
            print("\033[91m\nOpción no válida. Inténtelo nuevamente.\033[0m")
            time.sleep(2)
            os.system("clear")



