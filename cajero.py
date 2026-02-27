saldo_base = 0

while (saldo_base <= 0):
    try:
        saldo_base = int(input("Ingrese saldo inicial: "))
    except:
        print("Error. No ingreso un saldo valido!")

selection = ""

while (selection != "4"):
    print("\nMenu")
    print("1. Consultar saldo")
    print("2. Retirar saldo")
    print("3. Consignar saldo")
    print("4. Salir")
    
    selection = input("Seleccione el numero de operacion a realizar: ")
    
    if (selection == "1"):
        print("Operacion realizada! \nSu saldo actual es: ", saldo_base)
        
    elif (selection == "2"):
        
        cantidad_a_retirar = 0
        
        while (cantidad_a_retirar <=0):
            try:
                cantidad_a_retirar = int(input("Ingrese cantidad a retirar: "))
            except:
                print("Error. No ingreso una cantidad valida!")
                
            if cantidad_a_retirar > saldo_base:
                print("No se puede realizar la operacion, fondos insuficientes!")
            else:
                saldo_base = saldo_base-cantidad_a_retirar
                print("Operacion realizada! \nHa retirado: ", cantidad_a_retirar)
            
    elif (selection == "3"):
        
        valor_a_consignar = 0
        
        while (valor_a_consignar <=0):
            try:
                valor_a_consignar = int(input("Ingrese cantidad a consignar: "))
            except:
                print("Error. No ingreso una cantidad valida!")
            saldo_base = saldo_base+valor_a_consignar
            print("Operacion realizada! \nHa depositado: ", valor_a_consignar)
            
    elif (selection == "4"):
        print("Proceso finalizado")
    else:
        print("No selecciono un numero de operacion valido!")
        
