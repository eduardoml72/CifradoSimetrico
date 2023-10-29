import os
from funcionesCifrado import *

if __name__ == '__main__':
    try:
        #Definimos el directorio a cifrar
        directorio = "ArchivosCifrar"
        #Obtenermos archivos del directorio
        archivos = os.listdir(directorio)
        #Guardamos en una lista el path relativo de cada archivo
        todosArchivos = [directorio + '\\' + archivo for archivo in archivos]
        print(todosArchivos)
        #Generamos clave y almacenamos en variable
        generarClaves()
        clave = leerClaves()
        #Cifrado de archivos listados
        cifrado(todosArchivos, clave)
    except Exception as e:
        print(e)