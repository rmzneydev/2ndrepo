# Ejercicios con operadores aritméticos
# 3. Suma de dos números
# a. Pide al usuario dos números y muestra la suma de ambos.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
print("La suma de los dos números es:", suma)

# 4. Resta de dos números
# a. Pide al usuario dos números y muestra la resta del primero menos el
# segundo.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resta = num1 - num2
print("La resta de los dos números es:", resta)

# 5. Multiplicación de dos números
# a. Pide al usuario dos números y muestra el resultado de multiplicarlos.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
multiplicacion = num1 * num2
print("La multiplicación de los dos números es:", multiplicacion)

# 6. División de dos números
# a. Pide al usuario dos números y muestra el resultado de dividir el primero por
# el segundo.
# b. Asegúrate de que el segundo número no sea cero.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num2 != 0:
    division = num1 / num2
    print("La división de los dos números es:", division)
else:
    print("Error: No se puede dividir por cero.")
    
# 7. Promedio de tres números
# a. Pide al usuario tres números y muestra su promedio
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print("El promedio de los tres números es:", promedio)