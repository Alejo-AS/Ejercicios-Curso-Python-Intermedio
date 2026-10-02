#Práctica 2: Excepciones - TypeError

# Escribe un programa que intente sumar un número y una cadena. 
# Si se produce un error de tipo, captura la excepción TypeError y muestra 
# un mensaje de error al usuario.

try:
    numero = 42
    cadena = "hola que tal"
    resultado = numero + cadena
    print("Resultado:", resultado)
except TypeError:
    print("Error: no se puede sumar un número y una cadena.")

