#Práctica 2: Excepciones - KeyError

# Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
# Si se produce una excepción KeyError, captura la excepción y muestra

persona = {"nombre": "Alejo", "edad": 25} 

try: 
    print(persona["direccion"])
except KeyError:
    print("Error: la clave no existe en el diccionario.")