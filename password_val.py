password = "1835acfg"

entrada = input("Ingrese contraseña: ")

ar1 = list (entrada)
ar2 = list(password)

if len(ar1) == len(ar2):
    coincidencias = 0
    for i in range(len(ar2)):
        if ar1[i] == ar2[i]:
            coincidencias+=1
    if coincidencias == len(ar1):
        print("La contraseña es correcta!")
    else:
        print(f"Coincidencias: {coincidencias}")
    
else:
    print("El tamaño no coincide!")

