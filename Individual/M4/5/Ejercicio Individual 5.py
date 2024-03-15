from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,"es_ES")
class NoPrivilegeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
class Proyecto():
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        self.presupuesto=0
        self.tiempo_proyecto=90
    def __repr__(self) -> str:
        return self.nombre
class Usuario():
    def __init__(self,nombre_usuario,password,sueldo=0,**kwargs):
        self.nombre_usuario=nombre_usuario
        self.password=password
        self.sueldo=sueldo
        self.additional_info={i:kwargs[i] for i in kwargs}
    def getclass(self):
        return type(self).__name__
    def getjerarquia(self):
        raise TypeError
    def PuedeMandar(self,empleado):
        return self.getjerarquia()>empleado.getjerarquia()
    def getSueldo(self):
        return self.sueldo
    def __repr__(self) -> str:
        return self.nombre_usuario
class Gerente(Usuario):
    def __init__(self,nombre_usuario,password,sueldo):
        super().__init__(nombre_usuario,password,sueldo)
    def getjerarquia(self):
        return 1
    def CambiarSueldo(self,empleado,nuevo_sueldo):
        if self.PuedeMandar(empleado):
            empleado.sueldo=nuevo_sueldo
        else:
            raise NoPrivilegeError
    def CambiarPresupuesto(self,proyecto:Proyecto,nuevo_presupuesto):
        proyecto.presupuesto=nuevo_presupuesto
    def CrearProyecto(self,empresa,nombre):
        empresa.IngresarProyecto(Proyecto(nombre))
class Dueño(Usuario):
    def __init__(self,nombre_usuario,password,patrimonio):
        super().__init__(nombre_usuario,password)
        self.patrimonio=patrimonio
    def getjerarquia(self):
        return 2
    def expandirEmpresa(self,empresa,nuevo_numero):
        empresa.cantidad_empleados_max=nuevo_numero
    def definirEmpresa(self,empresa,tipo):
        empresa.tipo_empresa=tipo
    def crearEmpresa(self):
        empresa=Empresa()
        empresa.agregarDueño(self)
        return empresa
class Trabajador(Usuario):
    def __init__(self,nombre_usuario,password,sueldo):
        super().__init__(nombre_usuario,password,sueldo)
        self.hora_entrada=datetime(2024,1,1,8,0,0)
        self.hora_salida=datetime(2024,1,1,17,0,0)
    def getjerarquia(self):
        return 0
    def marcar_entrada(self,empresa,hora:datetime):
        status="A tiempo" if hora.time()<self.hora_entrada.time() else "Atrasado"
        empresa.relog.registrar("entrada",self.nombre_usuario,hora,status)
    def marcar_salida(self,empresa,hora:datetime):
        status="A tiempo" if hora.time()>self.hora_entrada.time() else "Sobretiempo"
        empresa.relog.registrar("salida",self.nombre_usuario,hora,status)
    def getSueldo(self):
        return self.sueldo()*1.2
class Operador(Trabajador):
    def __init__(self, nombre_usuario, password, sueldo):
        super().__init__(nombre_usuario, password, sueldo)
    def getSueldo(self):
        return self.sueldo*1.5
class Obrero(Trabajador):
    def __init__(self, nombre_usuario, password, sueldo):
        super().__init__(nombre_usuario, password, sueldo)
    def getSueldo(self):
        return self.sueldo*1.1
class Empresa():
    def __init__(self):
        self.empleados=[]
        self.proyectos=[]
        self.cantidad_empleado_max=200
        self.tipo_empresa=""
        self.relog=RelogControl()
    def agregarDueño(self,dueño):
        if dueño.getclass()=="Dueño":
            self.dueño=dueño
    def ingresarEmpleado(self,contratador:Usuario,trabajador):
        if contratador.getclass() in ["Dueño","Gerente"]:
            self.empleados.append(trabajador)
        else:
            raise NoPrivilegeError("los trabajadores no pueden agregar empleados")
    def despedirEmpleado(self,despedidor:Usuario,empleado:Usuario):
        if despedidor.PuedeMandar(empleado):
            self.empleados.remove(empleado)
    def IngresarProyecto(self,proyecto):
        self.proyectos.append(proyecto)

class RelogControl():
    def __init__(self) -> None:
        self.registro_ingresos=[]
        self.registro_salidas=[]
    def registrar(self,tipo,usuario,hora,status):
        if tipo=="entrada":
            self.registro_ingresos.append(Entrada(usuario,hora,status))
        elif tipo=="salida":
            self.registro_salidas.append(Salida(usuario,hora,status))
        else:
            pass
    def cantidadRetrasos(self,empleado):
        return len([i for i in self.registro_ingresos if i.status=="Atrasado" and i.usuario==empleado.usuario])
class RegistroRelog():
    def __init__(self):
        pass
    def __repr__(self) -> str:
        return str({"usuario":self.usuario,"dia": self.hora.strftime("%a, %b %d"),"status":self.status})
class Entrada(RelogControl):
    def __init__(self,usuario:str,hora:datetime,status:str):
        super().__init__()
        self.usuario=usuario
        self.hora=hora
        self.status=status
class Salida(RelogControl):
    def __init__(self,usuario:str,hora:datetime,status:str):
        super().__init__()
        self.usuario=usuario
        self.hora=hora
        self.status=status
#PRUEBA
#HERENCIA
#Dueño, Gerente y Trabajador son hijos de usuario
#Obrero y Operador son hijos de Trabajador


#Creamos un dueño para la empresa
#el dueño tiene un sueldo de 0 pero tiene un patrimonio a diferencia del resto de usuarios
propietario=Dueño("Larry","12345",1_000_000_000)

#El dueño crea una empresa
#solo un dueño puede crear una empresa
empresa=propietario.crearEmpresa()

#Creamos un gerente
gerente=Gerente("Juan","12354",1_000_000)

#solo los gerentes pueden crear proyectos
gerente.CrearProyecto(empresa,"lucho a luchin")

#creamos un trabajador que es un operador
harry=Operador("Harry","134567",300_000)
#el gerente ingresa a un nuevo empleado, solo los gerentes y dueños pueden hacer esto
empresa.ingresarEmpleado(gerente,harry)

#creamos un obrero
nuevo_obrero=Obrero("Pepe","123456",400_000)

#si harry intenta ingresar un empleado no podra
try:
    empresa.ingresarEmpleado(harry,nuevo_obrero)
except NoPrivilegeError:
    #el dueño ingresa al nuevo empleado
    empresa.ingresarEmpleado(propietario,nuevo_obrero)
finally:
    print("el dueño ingreso al empleado")

#el gerente puede cambiar el sueldo de los trabajadores
gerente.CambiarSueldo(empresa.empleados[0],400_000)

#harry puede ingresa su entrada
empresa.empleados[0].marcar_entrada(empresa,datetime.now())

usuario=Usuario("Peon","12345",decoy="este es un ejemplo",eliminable=True)
#se puede añadir informacion adicional al usuario
print(usuario.additional_info)

try:
    usuario.additional_info["nombre"]
except KeyError:
    pass
finally:
    usuario.additional_info["nombre"]="Juan"
    print("usuario tiene nombre ahora")

print(usuario.additional_info)
try:
    usuario.getjerarquia()
except TypeError:
    pass
finally:
    print("usuario invalido")
#el nuevo empleado marca entrada
nuevo_obrero.marcar_entrada(empresa,datetime.now())

#el obrero tiene un bono distinto al operador
print(f"harry ganar {int(empresa.empleados[0].getSueldo())} mientras que pepe gana {int(empresa.empleados[1].getSueldo())}")
print(f"es porque harry es un {empresa.empleados[0].getclass()} y pepe es un {empresa.empleados[1].getclass()}")

print(f"la empresa tiene {len(empresa.empleados)} empleados los cuales son {empresa.empleados}")

try:
    empresa.empleados[2]
except IndexError:
    print("empleado no existe")
