import funciones

listado = []
opcion = ()

while True:
    opcion == funciones.menu()

    if opcion == "1":
      funciones.registrar_trabajador(listado)
    
    elif opcion == "2":
       funciones.listar_trabajadores(listado)

    elif opcion == 3:
       cargo = input ("cargo :")
       funciones.crearplanilla (listado,cargo)

    elif opcion == 4:
         print (" salir")
         break
    else:
       print ("opcion incorrecta")

    
