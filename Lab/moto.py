from datetime import datetime
class motocicleta:
    estado="nuevo"
    def __init__(self,color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso,**kwargs):
        self.color=color
        self.matricula=matricula
        self.combustible_litros=combustible_litros
        self.numero_ruedas=numero_ruedas
        self.marca=marca
        self.modelo=modelo
        self.fecha_fabricacion=fecha_fabricacion
        self.velocidad_punta=velocidad_punta
        self.peso=peso
        self.additional_info={i:kwargs[i] for i in kwargs}
        self.motor=False
    def arrancar(self):
        if not self.motor:
            self.motor=not self.motor
            print("motor en marcha")
        else:
            print("el motor ya estaba en marcha")
    def detener(self):
        if self.motor:
            self.motor=not self.motor
            print("el motor se ha detenido")
        else:
            print("el motor ya estaba detenido")
moto=motocicleta("rojo","LX12GX",10,2,"Yamaha","Motor",datetime(2023,12,31),180,53)
moto2=motocicleta(matricula="ZX1F23",combustible_litros=0,marca="chevrolet",fecha_fabricacion=datetime.now(),velocidad_punta=100,color="azul",peso=20,numero_ruedas=2,modelo="cabria")
moto.arrancar()
moto.detener()

moto.precio=740_990

print(f"el precio de {moto.marca} {moto.modelo} es de ${moto.precio}")

def ver_precio(self):
    print(f"el precio de {self.marca} {self.modelo} es de ${self.precio}")

motocicleta.ver_precio=ver_precio

moto.ver_precio()

try:
    moto2.ver_precio()
except:
    pass

def repostar(self):
    self.cantidad_combustible()
    while 1:
        cantidad=input("cuanto combustible va a repostar?")
        if not cantidad.isdigit():
            print("monto invalido")
            continue
        if int(cantidad)+self.combustible_litros>self.max_combustible:
            print("Maximo excedido")
            continue

        self.combustible_litros+=int(cantidad)
        break
    print(f"la moto {self.modelo} tiene {self.combustible_litros} litros en el estanque")
def cantidad_combustible(self):
    print(f"Reporte de la motocicleta {self.modelo} marca {self.marca}")
    print(f"la motocicleta tiene {self.combustible_litros} litros en el tanque\nse puede llenar un maximo de {self.max_combustible}\ny le faltan {self.max_combustible-self.combustible_litros} litros para estar al maximo")

moto.max_combustible=20
moto2.max_combustible=17
motocicleta.repostar=repostar
motocicleta.cantidad_combustible=cantidad_combustible

moto.repostar()
print(moto.combustible_litros)
