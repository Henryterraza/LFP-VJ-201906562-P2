import A_lexico

def Aplicacion():
    salir=False

    while not salir:
        print(
'''
-----------MENU-----------
1. Archivo
2. Nombre del archivo
3. salir
''')
        opcion=input("=>")
        if opcion=="1":
            directorio=input("Ingrese el directorio del archivo \n>> ")
            
            try:
                archivo=open(directorio, encoding="utf8").read()
                A_lexico.run(archivo)
                print("Archivo leido con exito!")
            except:
                print("\nArchivo no encontrado!\n")     

        elif opcion=="2":
            nombre = input("Ingrese nombre del archivo \n>> ")
            A_lexico.GenerarHTML(nombre)
            print("Reporte generado con exito!")
        elif opcion == "3":
            salir = True
            print("Fin del programa!")
        else:
            print("Opcion no valida!")

Aplicacion()
