#para activar el entorno virtual se debe escribir .\.venv\Scripts\activate desde la carpeta raiz

#Trabajo hecho por:
#   Matias Muñoz 
#   Sebastian Trejo
#   Daniel Barrera
#   Eduardo Muñoz
from pprint import pprint
LISTA_PRODUCTOS={
    "Manzanas":500,
    "Peras":400,
    "Fideos":1990,
    "Atún":790,
    "Arroz":1590
}
pedido={}
total=0
for i in LISTA_PRODUCTOS:
    cantidad=input(f"Ingrese cantidad de {i}: ")
    while not cantidad.isdigit():
        cantidad=input(f"Ingrese un numero valido: ")
    cantidad=int(cantidad)
    pedido[i]={"cantidad":cantidad,"subtotal":cantidad*LISTA_PRODUCTOS[i]}
    total+=cantidad*LISTA_PRODUCTOS[i]
pprint({"compra":pedido,"Total(sin IVA)":total,"IVA":int(total*0.19),"Total":int(total+total*0.19)})