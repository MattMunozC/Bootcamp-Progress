from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,"es_ES")
class Proyecto():
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        self.presupuesto=0
        self.tiempo_proyecto=90
    def __repr__(self) -> str:
        return self.nombre
class Usuario():
    def __init__(self,nombre_usuario,password,sueldo=0,**kwargs):
        self.jerarquia={"Trabajador":0,"Gerente":1,"Dueño":2}
        self.nombre_usuario=nombre_usuario
        self.password=password
        self.sueldo=sueldo
        self.additional_info={kwargs[i]:i for i in kwargs}
    def getclass(self):
        return type(self).__name__
    def getjerarquia(self):
        return self.jerarquia[self.getclass()]
    def PuedeMandar(self,empleado):
        return self.getjerarquia()>empleado.getjerarquia()
    def __repr__(self) -> str:
        return self.nombre_usuario
class Gerente(Usuario):
    def __init__(self,nombre_usuario,password,sueldo):
        super().__init__(nombre_usuario,password,sueldo)
    def CambiarSueldo(self,empleado,nuevo_sueldo):
        if self.PuedeMandar(empleado):
            empleado.sueldo=nuevo_sueldo
    def CambiarPresupuesto(self,proyecto:Proyecto,nuevo_presupuesto):
        proyecto.presupuesto=nuevo_presupuesto
    def CrearProyecto(self,empresa,nombre):
        empresa.IngresarProyecto(Proyecto(nombre))
class Dueño(Usuario):
    def __init__(self,nombre_usuario,password,patrimonio):
        super().__init__(nombre_usuario,password)
        self.patrimonio=patrimonio
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
    def marcar_entrada(self,empresa,hora:datetime):
        status="A tiempo" if hora.time()<self.hora_entrada.time() else "Atrasado"
        empresa.relog.registrar("entrada",self.nombre_usuario,hora,status)
    def marcar_salida(self,empresa,hora:datetime):
        status="A tiempo" if hora.time()>self.hora_entrada.time() else "Sobretiempo"
        empresa.relog.registrar("salida",self.nombre_usuario,hora,status)
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
    def ingresarEmpleado(self,contratador:Usuario,nombre_usuario,password,sueldo):
        if contratador.getclass() in ["Dueño","Gerente"]:
            self.empleados.append(Trabajador(nombre_usuario,password,sueldo))
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
            self.registro_ingresos.append(RegistroRelog(usuario,hora,status))
        elif tipo=="salida":
            self.registro_salidas.append(RegistroRelog(usuario,hora,status))
        else:
            pass
    def cantidadRetrasos(self,empleado):
        return len([i for i in self.registro_ingresos if i.status=="Atrasado" and i.usuario==empleado.usuario])
class RegistroRelog():
    def __init__(self,usuario:str,hora:datetime,status:str):
        self.usuario=usuario
        self.hora=hora
        self.status=status
    def __repr__(self) -> str:
        return str({"usuario":self.usuario,"dia": self.hora.strftime("%a, %b %d"),"status":self.status})
#PRUEBA
a=Dueño("Larry","12345",1_000_000_000)
emp=a.crearEmpresa()
b=Gerente("Juan","12354",1_000_000)
b.CrearProyecto(emp,"lucho a luchin")
#print(emp.proyectos)
emp.ingresarEmpleado(b,"jarry","12345",1000)
#print(emp.empleados[0].sueldo)
b.CambiarSueldo(emp.empleados[0],4000)
#print(emp.empleados[0].sueldo)
emp.empleados[0].marcar_entrada(emp,datetime.now())
print(emp.relog.registro_ingresos)