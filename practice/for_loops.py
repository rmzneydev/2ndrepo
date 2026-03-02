# Ejercicios con ciclos "para"
# 17. Tabla de multiplicar
# a. Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10
# usando un ciclo para.
num = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    
# 18. Suma de los primeros N números naturales
# a. Pide al usuario un número N y muestra la suma de los números del 1 al N.

num = int(input("Ingrese un número para calcular la suma de los primeros N números naturales: "))
suma = 0
for i in range(1, num + 1):
    suma += i
print(f"La suma de los primeros {num} números naturales es: {suma}")

# 19. Mostrar los primeros N números pares
# a. Pide al usuario un número N y muestra los primeros N números pares.
num_pares = int(input("Ingrese un número para mostrar los primeros N números pares: "))
contador = 0
i = 0
while contador < num_pares:
    if i % 2 == 0:
        print(i)
        contador += 1
    i += 1

# 20. Factorial de un número
# a. Pide al usuario un número y calcula su factorial usando un ciclo par
num = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es: {factorial}") 