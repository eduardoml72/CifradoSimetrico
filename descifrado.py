import os
from funcionesCifrado import *

if __name__ == '__main__':
    try:
        # Definimos el directorio a descifrar
        directorio = "ArchivosCifrar"
        # Obtenermos archivos del directorio y guardamos en lista
        archivos = os.listdir(directorio)
        todosArchivos = [directorio + '\\' + archivo for archivo in archivos]
        #Obtenemos clave para descifrar
        clave = leerClaves()
        #Iniciamos con el descifrado de archivos
        descrifrado(todosArchivos, clave)

    except Exception as e:
        print(e)