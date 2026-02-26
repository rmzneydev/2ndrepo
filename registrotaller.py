print("Registro de Participantes - Taller de Programación")

### Registro inicial
cant_participantes = int(input("¿Cuántas personas desea registrar?: "))

### Registro por participante
for participante in range(cant_participantes):
    print("Registrando participante #" ,participante+1)
    nombre = input("Ingrese nombre: ")
    
    edad = -1
    ### Validación de edad      
    while (edad < 0):
        edad = int(input("Ingrese edad: "))
        if (edad < 0):
            print("¡La edad ingresada no es valida!")

    tiene_conocimientos = input("¿Tiene conocimientos básicos de computación? (si/no): ")
    
    ### Reglas para aceptar o rechazar
    if edad >=15 and tiene_conocimientos == "si":
        print("Puede participar en el taller.")
    else:
        print("No cumple los requisitos.")

### Mensaje final
print("Proceso finalizado.")