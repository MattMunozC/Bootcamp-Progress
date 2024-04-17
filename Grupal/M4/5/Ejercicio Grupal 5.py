from datetime import datetime
import random
from abc import ABC, abstractmethod
from exception import productExceedException,notEnoughInStoreException,NoPurchasesException
#Trabajo hecho por:
#   Matias Muñoz 
class Usuario(ABC):
    def __init__(self,nombre:str,apellido:str):
        self.nombre=nombre
        self.apellido=apellido
class Cliente(Usuario):
    __saldo=0
    def __init__(self,id_cliente:int,nombre:str,apellido:str,correo:str,fecha_registro:datetime,genero=None):
        super().__init__(nombre,apellido)
        self.id_cliente=id_cliente
        self.correo=correo
        self.fecha_registro=fecha_registro
        self.genero=genero
    def getSaldo(self)->int:
        return self.__saldo
    def setSaldo(self,saldo:int)->None:
        self.__saldo=saldo
class Proveedor():
    def __init__(self,run,nombre_legal,razon_social,pais,distincion="natural",fiel=0):
        self.run=run
        self.nombre_legal=nombre_legal
        self.razon_social=razon_social
        self.pais=pais
        self.distincion=distincion
        self.fiel=fiel

#CLASE PRODUCTO PADRE DE ELECTRODOMESTICOS Y LIBROS (ES UNA TIENDA RARA)
class Producto():
    __impuesto=1.19
    def __init__(self,SKU,nombre,categoria,proveedor:Proveedor,stock,valor_neto,estado="nuevo"):
        self.SKU=SKU
        self.nombre=nombre
        self.categoria=categoria
        self.proveedor:Proveedor=proveedor
        self.stock=stock
        self.valor_neto=valor_neto
        self.estado=estado
    def precioFinal(self):
        return int(self.valor_neto*self.__impuesto)
    def descontarStock(self):
        self.stock-=1
    def __str__(self) -> str:
        return f"{self.nombre}: {self.valor_neto*Producto.__impuesto}"
    def __repr__(self) -> str:
        return f"{self.nombre}: {self.valor_neto*Producto.__impuesto}"
    
class Electrodomestico(Producto):
    def __init__(self, SKU, nombre, categoria, proveedor: Proveedor, stock, valor_neto, estado="nuevo"):
        super().__init__(SKU, nombre, categoria, proveedor, stock, valor_neto, estado)
    def __str__(self):
        return super().__str__()        
class Libro(Producto):
    def __init__(self, SKU, nombre, categoria, proveedor: Proveedor, stock, valor_neto, estado="nuevo"):
        super().__init__(SKU, nombre, categoria, proveedor, stock, valor_neto, estado)
    def __str__(self):
        return super().__str__()
    

#BOLETA: una compra es una boleta antes de convertirse en una orden de compra
class Boleta():
    id_boleta=0
    def __init__(self,cliente:Cliente,vendedor):
        self.productos=[]
        self.subtotal=0
        self.iva=0
        self.id=Boleta.id_boleta
        self.cliente=cliente
        self.vendedor=vendedor
        Boleta.id_boleta+=1
    def agregar_producto(self,producto,cantidad):
        try:
            if cantidad>10:
                raise productExceedException
            detalle=DetalleBoleta(producto,cantidad)
            self.productos.append(detalle)
            self.subtotal+=(detalle.subtotal())
            self.iva+=detalle.iva()
        except productExceedException:
            print("Cantidad no puede superar los 10 productos")
    def total(self):
        return self.subtotal+self.iva
    def convertirOrdenCompra(self):
        return OrdenCompra(self.cliente,self.vendedor,self.productos)
    def __repr__(self) -> str:
        return f"boleta {self.id}\n\t{"\n\t".join([str(i) for i in self.productos])}\nsubtotal: {self.subtotal}\niva:{self.iva}\ntotal:{self.total()}"

#DETALLES DE LA BOLETA POR PRODUCTO
class DetalleBoleta():
    def __init__(self,producto:Producto,cantidad:int):
        self.producto=producto
        self.cantidad=cantidad
    def subtotal(self)->int:
        return self.producto.valor_neto*self.cantidad
    def iva(self):
        return int(self.producto.valor_neto*self.cantidad*0.19)
    def __str__(self):
        return f"producto: {self.producto.nombre} cantidad: {self.cantidad} subtotal: {self.subtotal()}"
class Vendedor(Usuario):
    __comision=0
    def __init__(self,run,nombre,apellido,seccion,contrato="planta"):
        super().__init__(nombre,apellido)
        self.run=run
        self.seccion=seccion
        self.contrato=contrato
    def getComision(self):
        return self.__comision
    def setComision(self,comision):
        self.__comision=comision
    def vender(self,producto:Producto,cliente:Cliente,cantidad:int=1,boleta:Boleta=None):
        #Tecnicamente sobrecarga ya que es el mismo metodo con distintos parametros 
        #no se puede hacer sobre carga si no es herencia lo cual podria hacerse si existiera una clase arriba de vendedor y cliente (persona)
        if isinstance(producto,Producto):
            if boleta==None: boleta=Boleta(cliente,self)
            producto.descontarStock()
            self.setComision(self.getComision()+int(producto.valor_neto*0.005))
            if cliente.getSaldo()-producto.precioFinal()<0.0:
                print("no tiene saldo suficiente")
                return None
            cliente.setSaldo(int(cliente.getSaldo()-producto.precioFinal()))
            boleta.agregar_producto(producto,cantidad)
        elif type(producto)==list:
            boleta=Boleta(cliente,self)
            for producto in producto:
                self.vender(producto,cliente,boleta=boleta)
        elif type(producto)==dict:
            boleta=Boleta(cliente,self)
            for prod in producto:
                self.vender(prod,cliente,boleta=boleta,cantidad=producto[prod])
        return boleta
class OrdenCompra(Boleta):
    id=0
    def __init__(self, cliente: Cliente, vendedor,productos,estado="Por enviar"):
        super().__init__(cliente, vendedor)
        try:
            if len(productos)<=0:
                raise NoPurchasesException
            OrdenCompra.id+=1
            self.id_compra=OrdenCompra.id
            self.productos=productos
            self.estado=estado
        except NoPurchasesException:
            print("el cliente no tiene compras")

    
class almacenamiento():
    def __init__(self)->None:
        self.inventario=[]
    def buscar_producto(self,producto,return_index=False):
        for count,i in enumerate(self.inventario):
            if i==producto:
                if return_index: return count
                return i
        return None
    def agregar_producto():
        pass

class Bodega(almacenamiento):
    def __init__(self) -> None:
        super().__init__()
    def agregar_producto(self,producto:Producto):
        self.inventario.append(producto)
class Sucursal(almacenamiento):
    def __init__(self) -> None:
        super().__init__()
        self.bodega=Bodega()
    def agregar_producto(self,producto:Producto,bodega=False):
        if bodega:
            self.bodega.agregar_producto(producto)
        else:
            self.inventario.append(producto)
    def verificar_existencia(self,producto):
        producto=self.buscar_producto(producto)
        if producto.stock<50:
            producto_bodega=self.bodega.buscar_producto(producto)
            try:
                if producto_bodega.stock<300:
                    raise notEnoughInStoreException("No hay suficiente en Bodega")
                self.bodega.inventario[self.bodega.buscar_producto(producto,True)][1]=producto_bodega.stock-300
                self.inventario[self.bodega.buscar_producto(producto,True)][1]=producto_bodega.stock+300
            except notEnoughInStoreException:
                print("No hay suficiente en bodega")


#EJEMPLO

#GENERADOR DE CORREOS
correo=lambda nombre,apellido:f"{nombre}.{apellido}@gmail.com"

#CLIENTES
cliente1=Cliente(1,"pedro","perez",correo("pedro","perez"),datetime.now())
cliente2=Cliente(2,"Oscar","Quinteros",correo("Oscar","Quintero"),datetime.now())
cliente3=Cliente(3,"Christian","Caracas",correo("Christian","caracas"),datetime.now())
cliente4=Cliente(4,"Pedro","Rumino",correo("pedro","rumino"),datetime.now())
cliente5=Cliente(5,"Fabricio","Copano",correo("Fabricio","Copano"),datetime.now())


#GENERADOR DE RUT
rut=lambda :"".join([str(random.randint(0,9)) for _ in range(0,9)])+f"-{random.randint(0,9)}"


#VENDEDORES
vendedor1=Vendedor(rut(),"pablo","pereira","Perfumeria")
vendedor2=Vendedor(rut(),"Michael","Urrutia","Perfumeria")
vendedor3=Vendedor(rut(),"Pedro","Riquelme","Perfumeria")
vendedor4=Vendedor(rut(),"Bernardo","O'higgins","Libreria")
vendedor5=Vendedor(rut(),"Marco","Mora","Libreria")

#SKU GENERATOR
letter="qwertyuiopasdfghjklñzxcvbnm"
random_letter=lambda : random.choice([letter.upper()[random.randint(0,len(letter))-1],letter.lower()[random.randint(0,len(letter)-1)],str(random.randint(0,9))])
SKU=lambda lensku:"".join([random_letter() for _ in range(lensku)])

producto1=Producto(SKU(10),"Zapatillas","Calzado","Adidas",20,9900)
producto2=Libro(SKU(10),"Weona, tú podí","Libro","Planetadelibros",10,6900)
producto3=Producto(SKU(10),"Laptop","computadores","HP",5,199990)
producto4=Electrodomestico(SKU(10),"Ventilador","Linea blanca","LG",40,19990)
producto5=Electrodomestico(SKU(10),"Lavadora","Linea Blanca","Samsung",2,599990)

cliente1.setSaldo(10_000_000)
a=vendedor1.vender(producto1,cliente1)
b=vendedor1.vender([producto2,producto3],cliente1)
c=vendedor1.vender([producto1,producto2,producto3,producto4,producto5],cliente1)

d=vendedor2.vender({producto1:12},cliente1)

sucursal=Sucursal()
sucursal.agregar_producto(producto1)
sucursal.agregar_producto(producto2)
sucursal.agregar_producto(producto3)
sucursal.agregar_producto(producto4)
sucursal.agregar_producto(producto5)

sucursal.agregar_producto(producto1,True)
sucursal.agregar_producto(producto2,True)
sucursal.agregar_producto(producto3,True)
sucursal.agregar_producto(producto4,True)
sucursal.agregar_producto(producto5,True)

sucursal.verificar_existencia(producto1)

print(sucursal.inventario)

boleta_vacia=Boleta(cliente1,vendedor1)
boleta_vacia.convertirOrdenCompra();
