#read.py
from termcolor import cprint
from pyfiglet import figlet_format
from cryptography.fernet import Fernet
import time, os

def generate_passwords_read():
    selected_color = "red"
    header_text = "Passwords"
    header = figlet_format(header_text)
    cprint(header, color=selected_color)

def descifrar_contraseña(contraseña_cifrada, clave_cifrado_usuario):
    fernet = Fernet(clave_cifrado_usuario)
    return fernet.decrypt(contraseña_cifrada.encode()).decode()

def ver_contraseñas(usuarios, usuario):
    usuario_actual = usuarios.find_one({"usuario": usuario})
    clave_cifrado_usuario = usuario_actual["clave_cifrado"].encode()
    contraseñas = usuario_actual.get("contraseñas", [])

    if not contraseñas:
        os.system("clear")
        print("\nNo hay contraseñas almacenadas.")
        time.sleep(2)
        return

    contraseñas.sort(key=lambda x: x.get("nombre_cuenta", "").lower())

    while True:
        os.system("clear")
        generate_passwords_read()
        print("Seleccione una cuenta para ver la información:\n")
        for i, contraseña in enumerate(contraseñas, 1):
            nombre_cuenta = contraseña.get("nombre_cuenta", "N/A")
            print(f"{i}. {nombre_cuenta}")

        try:
            seleccion = int(input("\nIngrese el número de la cuenta o 0 para salir: "))
            if seleccion == 0:
                break
            elif 1 <= seleccion <= len(contraseñas):
                mostrar_informacion(contraseñas[seleccion - 1], clave_cifrado_usuario)
            else:
                print("Número no válido. Inténtelo nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def mostrar_informacion(contraseña, clave_cifrado_usuario):
    contraseña_descifrada = descifrar_contraseña(contraseña.get('contraseña', 'N/A'), clave_cifrado_usuario)
    print("\nInformación de la cuenta:")
    print(f"Nombre de la cuenta: {contraseña.get('nombre_cuenta', 'N/A')}")
    print(f"Usuario: {contraseña.get('usuario', 'N/A')}")
    print(f"Contraseña: {contraseña_descifrada}")
    time.sleep(5)
