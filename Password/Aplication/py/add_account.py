# add_account.py
from termcolor import cprint
from pyfiglet import figlet_format
from getpass import getpass
from cryptography.fernet import Fernet
import time, os

def generate_add_account_header():
    selected_color = "green"
    header_text = "Agregar Cuenta"
    header = figlet_format(header_text)
    cprint(header, color=selected_color)

def generate_sign_in():
    selected_color = "green"
    header_text = "Sign In"
    header = figlet_format(header_text)
    cprint(header, color=selected_color)

def cifrar_contraseña(contraseña_plana, clave_cifrado_usuario):
    fernet = Fernet(clave_cifrado_usuario)
    return fernet.encrypt(contraseña_plana.encode()).decode()

def agregar_cuenta(usuarios, usuario):
    usuario_actual = usuarios.find_one({"usuario": usuario})
    clave_cifrado_usuario = usuario_actual["clave_cifrado"].encode()

    while True:
        os.system("clear")
        generate_add_account_header()
        print("\n1. Ingrese el nombre de la cuenta")
        print("2. Volver atrás")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            os.system("clear")
            generate_add_account_header()
            nombre_cuenta = input("Ingrese el nombre de la cuenta: ")
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            contraseña = getpass("Ingrese la contraseña: ")

            contraseña_cifrada = cifrar_contraseña(contraseña, clave_cifrado_usuario)

            usuarios.update_one(
                {"usuario": usuario},
                {"$push": {"contraseñas": {"nombre_cuenta": nombre_cuenta, "usuario": nombre_usuario, "contraseña": contraseña_cifrada}}},
            )
            print("\033[92m\nCuenta agregada con éxito.\033[0m")
            time.sleep(2)
            os.system("clear")
        elif opcion == "2":
            print("\033[92m\nVolviendo atrás al menú principal.\033[0m")
            time.sleep(2)
            os.system("clear")
            break
        else:
            print("\033[91m\nOpción no válida. Inténtelo nuevamente.\033[0m")
            time.sleep(2)
            os.system("clear")

def registrar_usuario(usuarios):
    while True:
        os.system("clear")
        generate_sign_in()
        print("\n1. Sing In")
        print("2. Volver atrás")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            os.system("clear")
            generate_sign_in()
            usuario = input("Ingrese un nombre de usuario: ")
            
            while True:
                contraseña = getpass("Ingrese una contraseña: ")
                confirmacion_contraseña = getpass("Confirme su contraseña: ")

                if contraseña == confirmacion_contraseña:
                    break
                else:
                    print("\033[91m\nLas contraseñas no coinciden. Inténtelo nuevamente.\n\033[0m")
                    time.sleep(2)
                    os.system("clear")
                    generate_sign_in()

            if usuarios.find_one({"usuario": usuario}):
                print("\033[91m\nEl nombre de usuario ya está registrado. Inténtelo nuevamente.\033[0m")
                time.sleep(2)
                os.system("clear")
            else:
                clave_cifrado = Fernet.generate_key().decode()
                usuarios.insert_one({"usuario": usuario, "contraseña": contraseña, "contraseñas": [], "clave_cifrado": clave_cifrado})
                print("\033[92m\nRegistro exitoso. Ahora puede iniciar sesión.\033[0m")
                time.sleep(2)
                os.system("clear")
                break
        elif opcion == "2":
            print("\033[92m\nVolviendo atrás al menú principal.\033[0m")
            time.sleep(2)
            os.system("clear")
            break
        else:
            print("\033[91m\nOpción no válida. Inténtelo nuevamente.\033[0m")
            time.sleep(2)
            os.system("clear")
