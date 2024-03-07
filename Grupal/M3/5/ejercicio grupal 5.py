import re
from time import sleep
#Trabajo hecho por:
#   Matias Muñoz 
#   Sebastian Trejo
#   Daniel Barrera
#   Eduardo Muñoz
opciones=["Agregar Cliente","Agregar Producto","Mostrar Clientes","Mostrar Productos","Eliminar Cliente","Eliminar Producto","salir"]
productos={}
clientes={}
id_autoincremental_cl=0
id_autoincremental_pr=0
patron_nombre=r"^[A-Za-záéíóúüñÁÉÍÓÚÜÑ][a-záéíóúüñ ]+$"
compraclientes={} #set
while len(clientes)<=10 and len(productos)<=5:
    eleccion=input("\t1. Agregar Cliente\n\t2. Agregar Producto\n\t3. Mostrar Clientes\n\t4. Mostrar Productos\n\t5. Eliminar Cliente\n\t6. Eliminar Producto\n\nseleccione una opcion:")
    if eleccion in opciones:
        if eleccion==opciones[0]:
            nombre=input("inserte un nombre: ")
            while not (bool(re.search(patron_nombre,nombre))):
                nombre=input("ingrese un nombre valido: ")
            edad=input("Ingrese su edad: ")
            while not edad.isdigit():
                edad=input("ingrese una edad correcta: ")
            clientes[str(id_autoincremental_cl)]={
                "nombre":nombre,
                "edad":int(edad)
            }
            id_autoincremental_cl+=1
            print("Cliente agregado con exito")
        if eleccion==opciones[1]:
            nombre=input("Ingrese nombre del producto: ")
            precio=input("Ingrese precio: ")
            while not precio.isdigit():
                precio=input("ingrese una edad correcta: ")
            color=input("Ingrese un color: ")
            productos[str(id_autoincremental_pr)]={
                "nombre":nombre,
                "precio":int(precio),
                "color":color
            }
            id_autoincremental_pr+=1
        if eleccion==opciones[2]:
            for i in clientes:
                sleep(2)
                print(f"Cliente {i}")
                sleep(3)
                print(f"\n\tnombre:{clientes[i]["nombre"]}\n\tedad:{clientes[i]["edad"]}")
        if eleccion==opciones[3]:
            for i in productos:
                sleep(2)
                print(f"producto {i}")
                sleep(3)
                print(f"\n\tnombre: {productos[i]["nombre"]}\n\tprecio: {productos[i]["precio"]}\n\tcolor: {productos[i]["color"]}")
        if eleccion==opciones[4]:
            delcli=input("Ingrese un id: ")
            #Se puede cambiar por un random value entre 0 y id_incremental_cl para eliminar un cliente al aza
            while not delcli.isdigit():
                delcli=input("ingrese un id valido")
            clientes.pop(delcli)
        if eleccion==opciones[5]:
            delcli=input("Ingrese un id: ")
            #se ingresa el valor de id_incremental_pr - 1 para borrar el ultimo valor
            while not delcli.isdigit():
                delcli=input("ingrese un id valido")
            clientes.pop(delcli)
        if eleccion==opciones[6]:
            break
    else:
        print("por favor, seleccione una opcion valida")
    print("\n\n")


#en caso de querer reemplazar las id
current=list(clientes.keys())    
print(current)
for i in current:
    clientes[f"{i}_piloto"]=clientes[i]
    clientes.pop(i)
current=list(clientes.keys())
print(current)
for i in current[:-4:]:
    clientes.pop(i)
print(clientes)
