repairs = []
requerimient = 0

while requerimient != 4:
    requerimient = int(input("----------------------------\nBienvenido\nIngrese\n1Para Registrar una reparacion\n2Para ver las reparaciones\n3Para remover una reparacion realizada\n4Salir\n------------------------------------\n"))
    validation = True
    match requerimient:
        case 1:
            repairs.append(input("Ingrese la nueva reparacion: "))

        case 2:
            print(repairs)
        case 3:
            while True:
                removee = input("Ingrese la reparacion realizada: ")
                
                if removee in repairs :
                    repairs.remove(removee)
                else :
                    print("¡La reparacion ingresada no se encuentra en la lista!")
        
            
                    
        case 4:
            print()
            
