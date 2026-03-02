# Ejercicios con ciclos "mientras"
# 13. Contador ascendente
# a. Pide al usuario un número y muestra una cuenta ascendente desde 1 hasta
# ese número usando un ciclo mientras.

num = int(input("Ingrese un número: "))
contador = 1
while contador <= num:
    print(contador)
    contador += 1  

# 14. Suma de números hasta ingresar 0 
# a. Pide al usuario números y súmalos.
# b. El programa debe detenerse cuando el usuario ingrese 0 y mostrar la suma
# total.

suma_total = 0
num = int(input("Ingrese un número (0 para terminar): "))
while num != 0:
    suma_total += num
    num = int(input("Ingrese un número (0 para terminar): "))
print("La suma total es:", suma_total)

# 15. Adivinar un número secreto
# a. Define un número secreto (por ejemplo, 7).
# b. Pide al usuario que adivine el número hasta que lo acierte.

numero_secreto = 7
adivinanza = int(input("Adivina el número secreto: "))
while adivinanza != numero_secreto:
    print("¡Incorrecto! Intenta de nuevo.")
    adivinanza = int(input("Adivina el número secreto: "))
print("¡Felicidades! Has adivinado el número secreto.")

# 16. Validar una contraseña
# a. Define una contraseña predefinida.
# b. Pide al usuario que ingrese una contraseña hasta que la escriba
# correctamente.

contraseña_predefinida = "contraseña123"
contraseña_ingresada = input("Ingrese la contraseña: ")
while contraseña_ingresada != contraseña_predefinida:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contraseña_ingresada = input("Ingrese la contraseña: ")
print("¡Contraseña correcta! Acceso concedido.")

