class Proyecto():
    def __init__(self) -> None:
        self.presupuesto=0
        self.tiempo_proyecto=90
class Usuario():
    def __init__(self,nombre_usuario,password):
        self.jerarquia={"Trabajador":0,"Gerente":1,"Dueño":2}
        self.nombre_usuario=nombre_usuario
        self.password=password
    def getclass(self):
        return type(self).__name__
    def getjerarquia(self):
        return self.jerarquia[self.getclass()]
    def PuedeMandar(self,empleado:Usuario):
        return self.getjerarquia()>empleado.getjerarquia()
class Gerente(Usuario):
    def __init__(self,nombre_usuario,password):
        super.__init__(nombre_usuario,password)
    def CambiarSueldo(self,empleado,nuevo_sueldo):
        if self.PuedeMandar(empleado):
            empleado.sueldo=nuevo_sueldo
    def CambiarPresupuesto(self,proyecto:Proyecto,nuevo_presupuesto):
        proyecto.presupuesto=nuevo_presupuesto
    def CrearProyecto(self,empresa):
        empresa.IngresarProyecto(Proyecto())
class Dueño(Usuario):
    def __init__(self,nombre_usuario,password):
        super.__init__(nombre_usuario,password)
    def expandirEmpresa(self,empresa,nuevo_numero):
        empresa.cantidad_empleados=nuevo_numero
class Trabajador(Usuario):
    def __init__(self,nombre_usuario,password,sueldo):
        super.__init__(nombre_usuario,password)
        self.sueldo=sueldo
class Empresa():
    def __init__(self):
        self.empleados=[]
        self.proyectos=[]
    def agregarDueño(self,dueño):
        if dueño.getclass()=="Dueño":
            self.dueño=dueño
    def ingresarEmpleado(self,contratador:Usuario,nombre_usuario,password):
        if contratador.getclass in ["Dueño","Gerente"]:
            self.empleados.append(Trabajador(nombre_usuario,password))
    def despedirEmpleado(self,despedidor:Usuario,empleado:Usuario):
        if despedidor.PuedeMandar(empleado):
            self.empleados.remove(empleado)
    def IngresarProyecto(self,proyecto):
        self.proyectos.append(proyecto)

