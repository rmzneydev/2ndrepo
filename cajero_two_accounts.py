account = 0

valid_account = False

while not valid_account:
    try:
        account = int(input("\nQue cuenta desea usar? (1 o 2): "))
        if account == 1 or account == 2:
            valid_account = True
        else:
            print("No existe la cuenta #",account)
    except ValueError:
        print("¡No ingreso un valor numerico! ")

saldo_cuenta_1 = 50000
saldo_cuenta_2 = 100000

selection = ""

while (selection != "5"):
    print(f"\n¡Esta logeado en su cuenta #{account}!")
    print("Menu")
    print("1. Consultar saldo")
    print("2. Retirar saldo")
    print("3. Consignar saldo")
    print("4. Cambiar de Cuenta")
    print("5. Salir")
    
    selection = input("Seleccione el numero de operacion a realizar: ")
    
    if (selection == "1"): ### Consultar Saldo
        print("\nOperacion realizada!")
        print(f"Su saldo actual es: {saldo_cuenta_1 if account == 1 else saldo_cuenta_2}")
                
    elif (selection == "2"): ### Retirar Saldo
        
        cantidad_a_retirar = 0.0
        valid_amount = False

        while not valid_amount:
            try:
                cantidad_a_retirar = input("\nIngrese cantidad a retirar: ")
                cantidad_a_retirar = float(cantidad_a_retirar.replace(",", "."))
                if (cantidad_a_retirar <= 0.0):
                    print("\nLa cantidad a retirar debe ser mayor a cero")
                else:
                    valid_amount = True
            except ValueError:
                print("Error: No ingreso una cantidad valida!")

        impuesto = cantidad_a_retirar * 0.004
    
        retiro_completado = False
        if (account == 1):
            if (cantidad_a_retirar > saldo_cuenta_1):
                print("\nNo se puede retirar:", cantidad_a_retirar, "- Saldo insuficiente")
            else:
                saldo_despues_retiro = saldo_cuenta_1 - cantidad_a_retirar
                if (saldo_despues_retiro >= impuesto):
                    saldo_cuenta_1 -= (cantidad_a_retirar + impuesto)
                    print(f"Se le descontara el impuesto en su cuenta #{account}")
                    retiro_completado = True
                else:
                    print(f"Su cuenta #{account} no tiene saldo suficiente para cubrir el impuesto")
                    print(f"Revisando cuenta #2...")
                    impuesto_faltante = impuesto - saldo_despues_retiro
                    if (saldo_cuenta_2 >= impuesto_faltante):
                        saldo_cuenta_1 = 0
                        saldo_cuenta_2 -= impuesto_faltante
                        print(f"Se descontaran {impuesto_faltante} de la cuenta #2 para cubrir impuesto")
                        retiro_completado = True
                    else:
                        print("No se puede continuar: saldo insuficiente para cubrir el impuesto")
        
        if (account == 2):
            if (cantidad_a_retirar > saldo_cuenta_2):
                print("\nNo puede retirar:", cantidad_a_retirar, "- Saldo insuficiente")
            else:
                saldo_despues_retiro = saldo_cuenta_2 - cantidad_a_retirar
                if (saldo_despues_retiro >= impuesto):
                    saldo_cuenta_2 -= (cantidad_a_retirar + impuesto)
                    print(f"Se le descontara el impuesto en su cuenta #{account}")
                    retiro_completado = True
                else:
                    print(f"Su cuenta #{account} no tiene saldo suficiente para cubrir el impuesto")
                    print(f"Revisando cuenta #1...")
                    impuesto_faltante = impuesto - saldo_despues_retiro
                    if (saldo_cuenta_1 >= impuesto_faltante):
                        saldo_cuenta_2 = 0
                        saldo_cuenta_1 -= impuesto_faltante
                        print(f"Se descontaran {impuesto_faltante} de la cuenta #1 para cubrir impuesto")
                        retiro_completado = True
                    else:
                        print("¡No se puede continuar: saldo insuficiente para cubrir el impuesto!")
                        
        if retiro_completado:
            print("\nOperacion realizada!")        
            print(f"Total retirado: {cantidad_a_retirar}")
            print(f"Su nuevo saldo en la cuenta {account} es: {saldo_cuenta_1 if account == 1 else saldo_cuenta_2}")
            
    elif (selection == "3"): ### Consignar Saldo

        valid_amount = False

        while not valid_amount:
            try:
                valor_a_consignar = input("Ingrese cantidad a consignar: ")
                valor_a_consignar = float(valor_a_consignar.replace(",", "."))

                if (valor_a_consignar <= 0.0):
                    print("\nLa cantidad a consignar debe ser mayor a cero")
                else:
                    valid_amount = True                
            except ValueError:
                print("Error: No ingreso una cantidad valida!")
        
        if (account == 1):
            saldo_cuenta_1 += valor_a_consignar
        else:
            saldo_cuenta_2 += valor_a_consignar
        
        print("\nOperacion realizada!")        
        print(f"Su nuevo saldo es:  {saldo_cuenta_1 if account == 1 else saldo_cuenta_2}")

            
    elif (selection == "4"): ### Cambiar de Cuenta
        account = 2 if (account == 1) else 1

    elif (selection == "5"): ### Consultar Salir
        print("Proceso finalizado.")
    else:
        print("\nNo ingreso un numero de operacion valido!")