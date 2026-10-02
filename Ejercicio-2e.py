#Práctica 2: Excepciones - ZeroDivisionError y ValueError

# Escribe un programa que intente dividir dos números. 
# Si el segundo número es cero, captura la excepción ZeroDivisionError. 
# Si el primer número es un número no válido, captura la excepción ValueError. 
# En cualquier caso, muestra un mensaje de error al usuario.

try:
    a = float(input("Ingresa el dividendo: "))
    b = float(input("Ingresa el divisor: "))
    resultado = a / b
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
except ValueError:
    print("Error: ingresaste un valor que no es un número válido.")