from datetime import datetime
import random
from abc import ABC, abstractmethod
#Trabajo hecho por:
#   Matias Muñoz 
#   Sebastian Trejo
#   Daniel Barrera
#   Eduardo Muñoz
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
        detalle=DetalleBoleta(producto,cantidad)
        self.productos.append(detalle)
        self.subtotal+=(detalle.subtotal())
        self.iva+=detalle.iva()
    def total(self):
        return self.subtotal+self.iva
    def convertirEnvio(self):
        return Envio(self.cliente,self.vendedor,self.productos)
    def __repr__(self) -> str:
        return f"boleta {self.id}\n\t{"\n\t".join([str(i) for i in self.productos])}\nsubtotal: {self.subtotal}\niva:{self.iva}\ntotal:{self.total()}"
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
        return boleta
class Envio(Boleta):
    def __init__(self, cliente: Cliente, vendedor,productos,estado="Por enviar"):
        super().__init__(cliente, vendedor)
        self.productos=productos
        self.estado=estado
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

correo=lambda nombre,apellido:f"{nombre}.{apellido}@gmail.com"
cliente1=Cliente(1,"pedro","perez",correo("pedro","perez"),datetime.now())
cliente2=Cliente(2,"Oscar","Quinteros",correo("Oscar","Quintero"),datetime.now())
cliente3=Cliente(3,"Christian","Caracas",correo("Christian","caracas"),datetime.now())
cliente4=Cliente(4,"Pedro","Rumino",correo("pedro","rumino"),datetime.now())
cliente5=Cliente(5,"Fabricio","Copano",correo("Fabricio","Copano"),datetime.now())

rut=lambda :"".join([str(random.randint(0,9)) for _ in range(0,9)])+f"-{random.randint(0,9)}"
vendedor1=Vendedor(rut(),"pablo","pereira","Perfumeria")
vendedor2=Vendedor(rut(),"Michael","Urrutia","Perfumeria")
vendedor3=Vendedor(rut(),"Pedro","Riquelme","Perfumeria")
vendedor4=Vendedor(rut(),"Bernardo","O'higgins","Libreria")
vendedor5=Vendedor(rut(),"Marco","Mora","Libreria")


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

print(c)
print(Usuario(nombre="a",apellido="b"))