#Trabajo hecho por:
#   Matias Muñoz 
#   Sebastian Trejo
#   Daniel Barrera
#   Eduardo Muñoz

#Control de Bodega
def CrearBodega():
    productos = {
        1: {"nombre": "AquaGlow LED Showerhead", "precio": 4999, "stock": 50},
        2: {"nombre": "SmartPlant Assistant", "precio": 3999, "stock": 30},
        3: {"nombre": "SonicSleep Therapy System", "precio": 7999, "stock": 20},
        4: {"nombre": "TechTracker Key Finder", "precio": 1999, "stock": 100},
        5: {"nombre": "Gourmet Spice Blends Set", "precio": 2999, "stock": 40},
        6: {"nombre": "ZenDesk Meditation Chair", "precio": 14999, "stock": 10},
        7: {"nombre": "EcoFresh Food Storage Containers", "precio": 2499, "stock": 60},
        8: {"nombre": "SolarGlow Pathway Lights", "precio": 3499, "stock": 25},
        9: {"nombre": "FitFuel Portable Blender", "precio": 5999, "stock": 15},
        10: {"nombre": "Artisan Chocolate Sampler", "precio": 1999, "stock": 50},
        11: {"nombre": "Stylish Wireless Headphones", "precio": 5999, "stock": 35},
        12: {"nombre": "Smart Home Security Camera", "precio": 8999, "stock": 10},
        13: {"nombre": "Electric Wine Opener Set", "precio": 4999, "stock": 20},
        14: {"nombre": "Luxury Bath Towel Set", "precio": 3999, "stock": 45},
        15: {"nombre": "Portable Outdoor Grill", "precio": 7999, "stock": 5}
    }
    return productos
def AgregarProducto(bodega):
    nombre=input("nombre del producto: ")
    precio=input("precio: ")
    #repitira hasta que ingrese un entero
    while not precio.isdigit():
        precio=input("ingrese un precio valido: ")
    stock=input("stock: ")
    #repetira hasta que ingrese un entero
    while not stock.isdigit():
        stock=input("ingrese un stock valido: ")
    #genera el id del siguiente producto buscando el valor maximo actual y sumando 1
    id=max(*list(bodega.keys()))+1
    bodega[id]={"nombre":nombre,
                "precio":int(precio),
                "stock":int(stock)
                }
    return None
def ActualizarProducto(bodega,id,cantidad):
    #suma la nueva cantidad al stock
    bodega[id]["stock"]+=cantidad
    return None
def BuscarProducto(bodega,producto):
    #busca un producto por nombre y lo regresa
    for id in bodega:
        if bodega[id]["nombre"]==producto:
            return bodega[id]
    return None
def Disponibilidad(bodega):
    #filtra la bodega para sacar lo que sea 0
    bodega_filtrada=FiltrarBodega(bodega,1)
    for id in bodega_filtrada:
        print(f"{bodega[id]["nombre"]}: {bodega[id]["stock"]} {"unidad disponible" if bodega[id]["stock"]==1 else "unidades disponibles"}")
    return None
def DisponibilidadId(bodega,id):
    #busca la disponibilidad de un producto por id
    print(f"{bodega[id]["nombre"]}: {bodega[id]["stock"]} {"unidad disponible" if bodega[id]["stock"]==1 else "unidades disponibles"}")
    return bodega[id]
def DisponibiildadNombre(bodega,nombre):
    #busca la disponibilidad de un producto por nombre
    producto=BuscarProducto(bodega,nombre)
    print(f"{producto["nombre"]}: {producto["stock"]} {"unidad disponible" if producto["stock"]==1 else "unidades disponibles"}")
    return producto
def ListarProductos(bodega):
    #regresa una lista de nombres de los productos
    return [i["nombre"] for i in bodega]
def FiltrarBodega(bodega,min):
    #filtra la bodega de acuerdo al criterio del stock minimo
    return {i:bodega[i] for i in bodega if bodega[i]["stock"]>=min}

#Control de ventas
def Existe(bodega,id,cantidad):
    return bodega[id]["stock"]>cantidad
def TotalClientes(clientes):
    print(f"Total de clientes: {len(list(clientes.keys()))}")
    return len(list(clientes.keys()))
def Comprar(bodega,compras,clientes,cliente, producto,cantidad=1):
    
    cliente=clientes.get(cliente,None)
    producto_id=producto
    producto=bodega.get(producto,None)
    if cliente==None or producto==None:
        print(f"id del {"cliente" if cliente==None else "producto"} no encontrada")
        return None
    if producto["stock"]<cantidad:
        print("Compra Cancelada")
        return None
    if not Existe(bodega,producto_id,cantidad):
        print("Compra Cancelada")
        return None
    AutorizarCompra(bodega,compras,cliente["nombre"],producto["nombre"],cantidad)
    print("Compra completada y enviada")
def AutorizarCompra(bodega,compras,cliente,producto,cantidad):
    bodega[producto]["stock"]-=cantidad
    compras.append((producto,cliente,cantidad))
    return None

clientes = {
    1: {"nombre": "Alice Johnson", "usuario": "ajohnson82"},
    2: {"nombre": "David Smith", "usuario": "dsmith345"},
    3: {"nombre": "Emily Chen", "usuario": "echen17"},
    4: {"nombre": "Michael Thompson", "usuario": "mthompson99"},
    5: {"nombre": "Sarah Rodriguez", "usuario": "srodriguez23"},
    6: {"nombre": "Christopher Lee", "usuario": "clee2000"},
    7: {"nombre": "Jessica Baker", "usuario": "jbaker88"},
    8: {"nombre": "Matthew Davis", "usuario": "mdavis456"},
    9: {"nombre": "Ashley Martinez", "usuario": "amartinez77"},
    10: {"nombre": "Daniel Nguyen", "usuario": "dnguyen123"},
    11: {"nombre": "Samantha Wilson", "usuario": "swilson55"},
    12: {"nombre": "Andrew Taylor", "usuario": "ataylor301"},
    13: {"nombre": "Jennifer Garcia", "usuario": "jgarcia101"},
    14: {"nombre": "Ryan Harris", "usuario": "rharris22"},
    15: {"nombre": "Megan Clark", "usuario": "mclark789"},
    16: {"nombre": "Kevin Turner", "usuario": "kturner45"},
    17: {"nombre": "Lauren Evans", "usuario": "levans567"},
    18: {"nombre": "Joshua Walker", "usuario": "jwalker2022"},
    19: {"nombre": "Amanda Thomas", "usuario": "athomas777"},
    20: {"nombre": "Brandon White", "usuario": "bwhite1996"}
}
compras=[]
bodega=CrearBodega()
AgregarProducto(bodega)
ActualizarProducto(bodega,3,10)
FiltrarBodega(bodega,5)
Disponibilidad(bodega)
TotalClientes(clientes)
Comprar(bodega,compras,clientes,2,4,3)