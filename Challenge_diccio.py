


cajero = {
    "saldo" : 0
}
menu = 0
while menu !=4 :
    while True:
        try : 
            menu = int(input("Ingrese\n1 Para despositar\n2 Para retirar\n3 Para consultar saldo\n4 Para salir: "))
            match menu:
                case 1:
                    deposit = int(input("Ingrese el valor a depositar: "))
                    cajero["saldo"] = cajero["saldo"]+deposit  
                    print("Deposito realizado")
                    
                    break
                    
                case 2:
                    deposit = int(input("Ingrese el valor a depositar: "))
                    cajero["saldo"] = cajero["saldo"]-deposit 
                    print("Retiro realizado")
                    break
                case 3:
                    print(cajero["saldo"])
                    break
                
                case 4:
                    print("Adios")
                    break
                        
                case _: 
                    print("Ingrese un digito valido")
                    
        except : 
            print("Ingrese un caracter valido")
            
