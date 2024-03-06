#main.py
import random, os, time
from termcolor import cprint
from pyfiglet import figlet_format
from conexion import conectar_base_datos
from login import iniciar_sesion, generate_login
from read import ver_contraseñas
from add_account import agregar_cuenta, registrar_usuario, generate_add_account_header, generate_sign_in

# Definir título y formato
def generate_random_header():
    fonts = ["standard"]
    colors = ["red", "white"]

    selected_font = random.choice(fonts)
    selected_color = random.choice(colors)

    header_main = "3v4 Password"

    header = figlet_format(header_main, font=selected_font)

    cprint(header, color=selected_color)

def generate_title_main():
    selected_color = "magenta"
    header_text = "3V4 Project"
    header = figlet_format(header_text)
    cprint(header, color=selected_color)

def gestionar_contraseñas(usuarios, usuario):
    while True:
        
        os.system("clear")
        generate_random_header()
        print("\n1. Agregar cuenta")
        print("2. Ver contraseñas guardadas")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            os.system("clear")
            generate_add_account_header()
            agregar_cuenta(usuarios, usuario)
        elif opcion == "2":
            os.system("clear")
            ver_contraseñas(usuarios, usuario)
        elif opcion == "3":
            print("\033[92m\nVolviendo atrás al menú principal.\033[0m")
            time.sleep(2)
            os.system("clear")
            break
        else:
            print("\033[91m\nOpción no válida. Inténtelo nuevamente.\033[0m")
            time.sleep(3)

def main():
    os.system("clear")
    usuarios = conectar_base_datos()

    while True:
        os.system("clear")
        generate_title_main()
        print("By Judith Agudo and Fariña")
        time.sleep(1)
        os.system("clear")
        generate_random_header()
        print("\033[91mBienvenido al gestor de contraseñas\033[0m")
        print("\n1. Login")
        print("2. Sign In")
        print("3. Exit")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            os.system("clear")
            usuario = iniciar_sesion(usuarios)
            if usuario is not None:  # Si iniciar_sesion devuelve None, no continuar con la gestión de contraseñas
                gestionar_contraseñas(usuarios, usuario)
        elif opcion == "2":
            os.system("clear")
            registrar_usuario(usuarios)
        elif opcion == "3":
            os.system("clear")
            print("¡Hasta luego!")
            break
        else:
            print("\033[91m\nOpción no válida. Por favor, seleccione una opción válida.\033[0m")
            time.sleep(2)
            os.system("clear")

if __name__ == "__main__":
    main()
