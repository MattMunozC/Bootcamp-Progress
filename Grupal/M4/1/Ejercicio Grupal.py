from datetime import datetime
import random
#Trabajo hecho por:
#   Matias Muñoz 
#   Sebastian Trejo
#   Daniel Barrera
#   Eduardo Muñoz
class Cliente():
    __saldo=0
    def __init__(self,id_cliente:int,nombre:str,apellido:str,correo:str,fecha_registro:datetime):
        self.id_cliente=id_cliente
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.fecha_registro=fecha_registro
    def getSaldo(self)->int:
        return self.__saldo
    def setSaldo(self,saldo:int)->None:
        self.__saldo=saldo
    
class Producto():
    __impuesto=1.19
    def __init__(self,SKU,nombre,categoria,proveedor,stock,valor_neto):
        self.SKU=SKU
        self.nombre=nombre
        self.categoria=categoria
        self.proveedor=proveedor
        self.stock=stock
        self.valor_neto=valor_neto
class Vendedor():
    __comision=0
    def __init__(self,run,nombre,apellido,seccion):
        self.run=run
        self.nombre=nombre
        self.apellido=apellido
        self.seccion=seccion
    def getComision(self):
        return self.__comision
    
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
producto2=Producto(SKU(10),"Weona, tú podí","Libro","Planetadelibros",10,6900)
producto3=Producto(SKU(10),"Laptop","computadores","HP",5,199990)
producto4=Producto(SKU(10),"Ventilador","Linea blanca","LG",40,19990)
producto5=Producto(SKU(10),"Lavadora","Linea Blanca","Samsung",2,599990)

print(vendedor1.run)