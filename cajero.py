saldo_base = -1.0

while (saldo_base < 0.0):
    try:
        saldo_base = float(input("Ingrese saldo inicial: "))
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
        print("\nOperacion realizada! - Su saldo actual es: ", saldo_base)
        
    elif (selection == "2"):
        
        cantidad_a_retirar = ""
        
        while (type(cantidad_a_retirar) != float):
            try:
                cantidad_a_retirar = float(input("Ingrese cantidad a retirar: "))
                if cantidad_a_retirar > saldo_base or cantidad_a_retirar <=0.0:
                    print("No se puede realizar la operacion!")
                else:
                    saldo_base = saldo_base-cantidad_a_retirar
                    print("\nOperacion realizada! - Ha retirado: ", cantidad_a_retirar)
            except:
                print("Error. No ingreso una cantidad valida!")
                       
    elif (selection == "3"):
        
        valor_a_consignar = 0.0
        
        while (valor_a_consignar <=0.0):
            try:
                valor_a_consignar = float(input("Ingrese cantidad a consignar: "))
            except:
                print("Error. No ingreso una cantidad valida!")
            saldo_base = saldo_base+valor_a_consignar
            print("\nOperacion realizada! - Ha depositado: ", valor_a_consignar)
            
    elif (selection == "4"):
        print("Proceso finalizado.")
    else:
        print("No selecciono un numero de operacion valido!")
        
