# Ejercicios con operadores relacionales
# 8. Comparación de dos números
# a. Pide al usuario dos números y muestra si son iguales o cuál es mayor.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 == num2:
    print("Los dos números son iguales.")
elif num1 > num2:
    print("El primer número es mayor que el segundo.")
else:
    print("El segundo número es mayor que el primero.")
    
# 9. Mayor de tres números
# a. Pide al usuario tres números y muestra cuál es el mayor de ellos.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
    print("El primer número es el mayor.")
elif num2 >= num1 and num2 >= num3:
    print("El segundo número es el mayor.")
else:
    print("El tercer número es el mayor.")

# 10. Verificar si un número es positivo, negativo o cero
# a. Pide al usuario un número y muestra si es positivo, negativo o cero.

num = float(input("Ingrese un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    
# 11. Verificar si un número es par o impar
# a. Pide al usuario un número y muestra si es par o impar.
num = int(input("Ingrese un número entero: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    
# 12. Verificar si una persona es mayor de edad
# a. Pide al usuario su edad y muestra si es mayor o menor de edad (mayor o
# igual a 18 años).

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")    