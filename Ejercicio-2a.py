#Práctica 2: Excepciones - ZeroDivisionError

# Escribe un programa que intente dividir dos números. 
# Si el segundo número es cero, captura la excepción ZeroDivisionError y 
# muestra un mensaje de error al usuario.

try:
    a = float(input("Ingrese el dividendo: "))
    b = float(input("Ingrese el divisor: "))
    resultado = a / b
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")

