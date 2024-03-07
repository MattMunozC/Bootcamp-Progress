#Trabajo hecho por:
#   Matias Muñoz 
#   Sebastian Trejo
#   Daniel Barrera
#   Eduardo Muñoz
import random
from time import sleep
STOCK={"p1":120,"p2":150}
PROVEEDOR_STOCK=150
n_compras=0
while 1:
    sleep(3)
    product=random.choice(list(STOCK.keys()))
    n=random.randint(1,10)
    if STOCK[product]>n:
        STOCK[product]-=n
    if PROVEEDOR_STOCK>0:
        if STOCK["p1"]<100:
            STOCK["p1"]+=50
            print("p1 restock")
            PROVEEDOR_STOCK-=50
        if STOCK["p2"]<100:
            STOCK["p2"]+=50
            print("p2 restock")
            PROVEEDOR_STOCK-=50
    if n_compras==10:
        n_compras=0
        print(f"10 compras hechas:\n\tstock disponible: {STOCK}")
    if STOCK["p1"]<0 and STOCK["p2"]<0:
        break
    n_compras+=1
