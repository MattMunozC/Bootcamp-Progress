import random
from pprint import pprint


#Trabajo hecho por:
#   Matias Muñoz 
#   Sebastian Trejo
#   Daniel Barrera
#   Eduardo Muñoz
def seleccionar(productos_seleccionados,productos_disponibles):
    print(list(productos_disponibles.keys()))
    producto=input("Seleccione un producto: ")
    while producto not in productos:
        producto=input("Seleccione un producto valido: ")
    
    while 1:
        cantidad=input("Ingrese una cantidad:")
        if cantidad.isdigit():
            if productos_disponibles[producto]-int(cantidad)<0:
                print("no hay suficiente existencia")
            else:
                cantidad=int(cantidad)
                break
        else:
            print("Ingrese un numero valido")
    productos_disponibles[producto]-=cantidad
    productos_seleccionados[producto]+=cantidad
productos = [
    "Camiseta",
    "Pantalones",
    "Zapatos",
    "Sombrero",
    "Bufanda",
    "Guantes",
    "Abrigo",
    "Calcetines",
    "Gorra",
    "Vestido",
    "Sudadera",
    "Jeans",
    "Chaqueta",
    "Gafas de sol",
    "Bolso",
    "Reloj",
    "Pulsera",
    "Anillo",
    "Cinturón",
    "Botas"
]

productos_disponibles={i:random.randint(1,30) for i in productos}

productos_seleccionados={i:0 for i in productos}
opciones=["salir","ver productos disponibles","ver productos seleccionados","seleccionar producto"]
print("Bienvenido,",end=" ")
while 1:
    if len(productos_seleccionados)==0:
        print("por favor seleccione una de las siguientes opciones para continuar\n")
    else:
        print("Hola de nuevo, por favor seleccione una accion")
    print("\t*ver productos disponibles\n\t*ver productos seleccionados\n\t*seleccionar producto\n\t*salir")
    seleccion=input("escriba su eleccion: ")
    if seleccion not in opciones:
        continue
    else:
        if seleccion==opciones[0]:
            break
        elif seleccion==opciones[1]:
            pprint(productos_disponibles)
        elif seleccion==opciones[2]:
            pprint([i for i in productos_seleccionados if productos_seleccionados[i]>0])
        elif seleccion==opciones[3]:
            seleccionar(productos_seleccionados,productos_disponibles)
print("Hasta pronto")