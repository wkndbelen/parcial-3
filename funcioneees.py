import random
import config
listado = [
     "nombre",
     "apellido",
     "cargo",
     "sueldo_bruto"
]

cargo = [
    "CEO",
    "DESARROLLADOR",
    "ANALISTA DE DATOS"
]

opcion = ()

def generar_codigo ():
    return random.randint (1000,9999)

def menu ():


def registar_trabajador (listado):
     codigo = generar_codigo("")
     nombre = input("nombre :")
     apellido = input ("apellido:")
     cargo = input ("cargo :")
     sueldo_bruto = input ("sueldo bruto :")

     listado.append([codigo,nombre,apellido,cargo,sueldo_bruto])

def listar_trabajadores (listado):
     print(["nombre" , "apellido" , " cargo" , " sueldo bruto"])
     for trabajador in listado:
        print(f"{trabajador[0]}\t{trabajador [1]} \t {trabajador[2]}\t {trabajador[3]}\t {trabajador[4]}")

def registrar_planilla (listado,cargo):
        with open ("archivo.txt"),"w" as archivo:
            texto = ("archivo")

if cargo == "cargo":
     for trabajador in listado:
          if trabajador [3] == cargo:
               print (trabajador)
               print (" la planilla fue creada con exito")
               break
          else:
             print (" ha opcurrido un error al crear la planilla")