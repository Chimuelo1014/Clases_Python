def menu(): 
    
    print("Ingrese\n1 Para despositar\n2 Para retirar\n3 Para consultar saldo\n4 Para salir: ")
    return input("Seleccione una opción: ")


# def deposito() :
#     deposit = int(input("Ingrese el valor a depositar: "))
#                     cajero["saldo"] = cajero["saldo"]+deposit  
#                     print("Deposito realizado")
                    
                   


usuarios = [
    {
        "usuario" : "Samu1122@riwi.com" ,

        "contraseña" : "samuellindo"
    },
        
    {
        "usuario" : "Santi123@riwi.com" ,

        "contraseña" : "Santi123"

    },

    {

        "usuario" : "Juank@riwi.com" ,

        "contraseña" : "juan123"
    }

]






# def usuario1() :
# #  manda ya a lo principal mandando sus respectivos parametros

# def usuario2() :


# def usuario3() : 


# cajero = {
#     "saldo" : 0
# }





# match 









######PRINCIPAL
user = input("Ingrese su Usuario" \
": ")

for i in usuarios.keys : 
    if user is usuarios[i]["usuario"] :
        password = input("Ingrese su contraseña " \
        ":")
        for i in usuarios :
            if password in usuarios[i]["contraseña"] :
                print("Bienvendio")
            else :
                print("mala")
    else : 
        print("nada")








#     if usuario
# while True:
#     opcion = mostrar_menu()
#     if opcion == "1":
#         name = input("Nombre del producto: ").strip()
#         price = conv_float("Precio: ")
#         amount = conv_int("Cantidad: ")
#         if price is not None and amount is not None:
#             add_products(inventary, name, price, amount)
#     elif opcion == "2":
#         name = input("Nombre del producto a buscar: ").strip()
#         counsult_products(inventary, name)
#     elif opcion == "3":
#         name = input("Nombre del producto a actualizar: ").strip()
#         new_price = conv_float("Nuevo precio: ")
#         if new_price is not None:
#             update_prices(inventary, name, new_price)
#     elif opcion == "4":
#         name = input("Nombre del producto a eliminar: ").strip()
#         delete_product(inventary, name)
#     elif opcion == "5":
#         total_inventary(inventary)
#     elif opcion == "6":
#         print("¡Gracias por usar el sistema de inventario!")
#         break
#     else:
#         print("Opción inválida. Intente de nuevo.")



# menu = 0
# while menu !=4 :
#     while True:
#         try : 
#             menu = int(input("Ingrese\n1 Para despositar\n2 Para retirar\n3 Para consultar saldo\n4 Para salir: "))
#             match menu:
#                 case 1:
#                     deposit = int(input("Ingrese el valor a depositar: "))
#                     cajero["saldo"] = cajero["saldo"]+deposit  
#                     print("Deposito realizado")
                    
#                     break
                    
#                 case 2:
#                     deposit = int(input("Ingrese el valor a depositar: "))
#                     cajero["saldo"] = cajero["saldo"]-deposit 
#                     print("Retiro realizado")
#                     break
#                 case 3:
#                     print(cajero["saldo"])
#                     break
                
#                 case 4:
#                     print("Adios")
#                     break
                        
#                 case _: 
#                     print("Ingrese un digito valido")
                    
#         except : 
#             print("Ingrese un caracter valido")




            