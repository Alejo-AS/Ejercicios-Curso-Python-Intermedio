#Práctica 2: Excepciones - FileNotFoundError

# Escribe un programa que intente abrir un archivo que no existe. 
# Si se produce una excepción FileNotFoundError, captura la excepción y 
# muestra un mensaje de error al usuario. 
# Sin embargo, también intenta crear el archivo si no existe.

try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido:", contenido)
except FileNotFoundError:
    print("Error: el archivo no existe. A continuación se creará el archivo 'datos.txt'")
    with open("datos.txt", "w") as archivo:
        archivo.write("Archivo creado con éxito.\n")
    print("Archivo 'datos.txt' creado correctamente.")
