import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
#pip install cryptography

#Funcion para obtener la clave de cifrado del archivo
def leerClaves():
    return open("clave.key", "rb").read() #Lee la clave

#Funcion para generar la clave y almacenarla en un archivo
def generarClaves():
    bit = input("Ingresa el tipo de clave (128,192 o 256):\n")
    clave = AESGCM.generate_key(bit_length = int(bit)) #Genera clave de X bits
    print(clave)
    open("clave.key", "wb").write(clave) #Crea o reescribe el archivo

#Funcion para cifrar los archivos 128 bits
def cifrado(archivos, clave):
    aes = AESGCM(clave)
    #Abrimos todos los archivos de directorio
    for archivo in archivos:
        with open(archivo, "rb") as file:
            #Lee la informacion de cada archivo
            datosArchivo = file.read()
        #Iniciamos con el cifrado de los datos de cada archivo y guardamos en variable
        datosCifrados = aes.encrypt(clave, datosArchivo, None)
        #Reemplazamos la informacion del archivo
        with open(archivo, "wb") as file:
            file.write(datosCifrados)

#Funcion para descifrar los archivos
def descrifrado(archivos, clave):
    aes = AESGCM(clave)
    #Abrimos todos los archivos
    for archivo in archivos:
        with open(archivo, "rb") as file:
            #Leemos la informacion contenida en el archivo
            datosCifrados = file.read()
        #Inicia con el descifrado de la informacion del archivo
        datosDescifrados = aes.decrypt(clave, datosCifrados, None)
        #Reemplazamos la informacion cifrada con la descifrada
        with open(archivo, "wb") as file:
            file.write(datosDescifrados)