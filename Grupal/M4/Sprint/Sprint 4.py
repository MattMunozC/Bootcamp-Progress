from datetime import datetime,timedelta
import locale
import random
import re
import json
import inspect
from pprint import pprint
locale.setlocale(locale.LC_TIME,"es_ES")
class NoPrivilegeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
class NoArgumentFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
class Proyecto():
    def __init__(self,nombre,encargado=None,fecha_inicio=None) -> None:
        self.nombre=nombre
        self.presupuesto=0
        self.duracion=90
        self.miembros=[]
        self.fecha_inicio=fecha_inicio
        self.encargado=encargado
        self.tareas=[]
    def getFechaTermino(self):
        return self.fecha_inicio+timedelta(days=self.duracion)
    def cambiarDuracion(self,solicitante,nueva_duracion):
        if type(solicitante)!=Dueño:
            raise NoPrivilegeError
        else:
            self.duracion=nueva_duracion
    def agregarTareas(self,solicitante,nombre_tarea,duracion):
        if type(solicitante)!=Gerente and (solicitante!=self.encargado or self.encargado!=None):
            raise NoPrivilegeError
        else:
            self.tareas.append(Tarea(nombre_tarea,duracion))
    def __repr__(self) -> str:
        return self.nombre
class Tarea(Proyecto):
    def __init__(self, nombre,duracion) -> None:
        super().__init__(nombre)
        if duracion>super().duracion:
            raise OverflowError("Tiempo de tarea excede la duracion del proyecto")
class Usuario():
    contador=0
    def __init__(self,nombre_completo,telefono,edad,sueldo=0,password=None,**kwargs):
        self.nombre_usuario=Usuario.__username(nombre_completo)
        self.nombre_completo=nombre_completo
        self.telefono=telefono
        self.edad=edad
        if password==None: self.password=Usuario.createPassword(8)
        self.sueldo=sueldo
        self.additional_info={i:kwargs[i] for i in kwargs}
        self.id=Usuario.contador
        Usuario.contador+=1
    @staticmethod
    def __username(name:str)->dict:
        return "".join([name.split(" ")[0][:3:],name.split(" ")[1][:3:]])
    @staticmethod
    def createPassword(passlen:int)->str:
        #Variable que define el rango de caracteres permitidos
        letter="qwertyuiopasdfghjklñzxcvbnm"
        #random letter es una funcion anonima que entrega una funcion de la lista utilizando random.choice
        #opciones:
        #   letter.upper() son los caracteres admisibles en mayuscula: será un caracter en la posicion aleatorio entre 0 y la longitud de letter con 1 paso de desfase
        #   letter.upper() son los caracteres admisibles en minuscula: será un caracter en la posicion aleatorio entre 0 y la longitud de letter con 1 paso de desfase
        #   un valor aleatorio entre 0 o 9
        random_letter=lambda : random.choice([letter.upper()[random.randint(0,len(letter))-1],letter.lower()[random.randint(0,len(letter)-1)],str(random.randint(0,9))])
        while 1:
            #mientras la contraseña no sea valida, creara una nueva contraseña hasta encontrar una valida
            password="".join([random_letter() for i in range(passlen)])
            if Usuario.__validate(password):
                return password
    @staticmethod
    def __validate(password:str)->bool:
        mayus="[A-Z]"
        minus="[a-z]"
        num="[0-9]"
        if not bool(re.search(mayus,password)):
            return False
        if not bool(re.search(minus,password)):
            return False
        if not bool(re.search(num,password)):
            return False
        return True
    def getclass(self):
        return type(self).__name__
    def getjerarquia(self):
        raise TypeError("Acceso Denegado: Clase no implementada correctamete")
    def PuedeMandar(self,empleado):
        return self.getjerarquia()>empleado.getjerarquia()
    def getSueldo(self):
        return self.sueldo
    def __repr__(self) -> str:
        return self.nombre_usuario
class Gerente(Usuario):
    def __init__(self,nombre_completo,telefono,edad,sueldo):
        super().__init__(nombre_completo,telefono,edad,sueldo)
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
    def __init__(self,nombre_completo,telefono,edad,patrimonio):
        super().__init__(nombre_completo,telefono,edad)
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
    __modificador=1.2
    def __init__(self,nombre_completo,telefono,edad,sueldo):
        super().__init__(nombre_completo,telefono,edad,sueldo)
        self.hora_entrada=datetime(2024,1,1,8,0,0)
        self.hora_salida=datetime(2024,1,1,17,0,0)
    def getjerarquia(self):
        return 0
    def marcar_entrada(self,empresa,password="",hora:datetime=datetime.now()):
        if self in empresa.empleados:
            status="A tiempo" if hora.time()<self.hora_entrada.time() else "Atrasado"
            empresa.relog.registrar("entrada",self,password,hora,status)
        else:
            raise NoPrivilegeError("Empleado no encontrado")
    def marcar_salida(self,empresa,password="",hora:datetime=datetime.now()):
        if self in empresa.empleados:
            status="A tiempo" if hora.time()>self.hora_entrada.time() else "Sobretiempo"
            empresa.relog.registrar("salida",self,password,hora,status)
        else:
            raise NoPrivilegeError("Empleado no encontrado")
    def getSueldo(self,modificador=None):
        try:
            return self.sueldo*modificador
        except TypeError:
            return self.sueldo*Trabajador.__modificador
    
#Operador y Obrero tienen modificadores distintos 
class Operador(Trabajador):
    __modificador=1.5
    def __init__(self,nombre_completo,telefono,edad,sueldo):
        super().__init__(nombre_completo,telefono,edad,sueldo)
    def getSueldo(self):
        return super().getSueldo(Operador.__modificador)
class Obrero(Trabajador):
    __modificador=1.0
    def __init__(self,nombre_completo,telefono,edad,sueldo):
        super().__init__(nombre_completo,telefono,edad,sueldo)
    def getSueldo(self):
        return super().getSueldo(Obrero.__modificador)
class Empresa():

#Empresa solo puede ser instanciada una vez
    _self = None
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    def __init__(self):
        self.empleados=[]
        self.proyectos=[]
        self.gerentes=[]
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
    def ingresaGerente(self,contratador:Usuario,gerente):
        if type(contratador)==Dueño:
            self.gerentes.append(gerente)
        else:
            raise NoPrivilegeError("los trabajadores no pueden agregar empleados")    
    def despedirEmpleado(self,despedidor:Usuario,empleado:Usuario):
        if despedidor.PuedeMandar(empleado):
            self.empleados.remove(empleado)
    def IngresarProyecto(self,proyecto):
        self.proyectos.append(proyecto)
    def __repr__(self) -> str:
        return str(self.__dict__)
#El empleado marca su entrada, 
#Relog es un componente de la empresa por lo que no es necesario explicar en que empresa se encuentra
class RelogControl():
    def __init__(self) -> None:
        self.registro_ingresos=[]
        self.registro_salidas=[]
    def registrar(self,tipo,usuario,password,hora,status):
        if tipo=="entrada" and usuario.password==password:
            self.registro_ingresos.append(Entrada(usuario,hora,status))
        elif tipo=="salida" and usuario.password==password:
            self.registro_salidas.append(Salida(usuario,hora,status))
        else:
            raise 
    def cantidadRetrasos(self,empleado):
        return len([i for i in self.registro_ingresos if i.status=="Atrasado" and i.usuario==empleado.usuario])
    def __repr__(self) -> str:
        return str({"Registro Entrada":self.registro_ingresos,"Registro Salida":self.registro_salidas})

#Un registro del relog es una clase abstracta que será definida como Entrada o Salida
class RegistroRelog():
    def __init__(self):
        pass
    def __repr__(self) -> str:
        return str({"usuario":self.usuario,"dia": self.hora.strftime("%a, %b %d"),"status":self.status})
    
#Realizacion de Registro Relog
class Entrada(RegistroRelog):
    def __init__(self,usuario:str,hora:datetime,status:str):
        super().__init__()
        self.usuario=usuario
        self.hora=hora
        self.status=status
#Realizacion de Registro Relog
class Salida(RegistroRelog):
    def __init__(self,usuario:str,hora:datetime,status:str):
        super().__init__()
        self.usuario=usuario
        self.hora=hora
        self.status=status


def normalize(item:object):
    if type(item)==datetime:
        return {"day":item.day,"month":item.month,"year":item.year,"hour":item.hour,"minute":item.minute,"seconds":item.second}
    if isinstance(item,Usuario):
        return {key:normalize(value) for key,value in item.__dict__.items()}
    else:
        return item

def extract(empresa:Empresa):
    with open("empresa.json","w",encoding="utf-8") as archivo:
        empleados=[{"type":type(i).__name__,"content":normalize(i)} for i in empresa.empleados]
        entrada=[{"type":type(i).__name__,"content":{key:normalize(value) for key,value in i.__dict__.items()}} for i in empresa.relog.registro_ingresos]
        salida=[{"type":type(i).__name__,"content":{key:normalize(value) for key,value in i.__dict__.items()}} for i in empresa.relog.registro_salidas]
        dueño={"type":type(empresa.dueño).__name__,"content":{key:value for key,value in empresa.dueño.__dict__.items()}}
        gerentes=[{"type":type(i).__name__,"content":normalize(i)} for i in empresa.gerentes]
        serializable={}
        for attribute,content in empresa.__dict__.items():
            try:         
                content={key:normalize(value) for key,value in content.__dict__.items()}
                serializable[attribute]={"type":type(content).__name__,"content":content}
            except:
                serializable[attribute]=empresa.__dict__[attribute]
        serializable["relog"]["content"]["registro_ingresos"]=entrada
        serializable["relog"]["content"]["registro_salidas"]=salida
        serializable["empleados"]=empleados
        serializable["dueño"]=dueño
        serializable["gerentes"]=gerentes
        serializable["proyectos"]=[{"type":type(i).__name__,"content":{key:normalize(value) for key,value in i.__dict__.items()}} for i in empresa.proyectos]
        empresa.serializable=serializable
        json.dump(serializable,archivo,ensure_ascii=False,indent=4)  
def load():
    with open("empresa.json","r",encoding="utf-8") as archivo:
        archivo=json.load(archivo)
        propietario=archivo["dueño"]["content"]
        propietario:Dueño=eval(archivo["dueño"]["type"])(*getargs(propietario,archivo["dueño"]["type"]))
        empresa=propietario.crearEmpresa()
        #esto es porque solo hay un gerente, nada más
        gerente=archivo["gerentes"][0]["content"]
        gerente:Gerente=eval(archivo["gerentes"][0]["type"])(*getargs(gerente,archivo["gerentes"][0]["type"]))
        empresa.ingresaGerente(propietario,gerente)
        empleados=[eval(archivo["empleados"][count]["type"])(*getargs(archivo["empleados"][count]["content"],archivo["empleados"][count]["type"])) for count,_ in enumerate(archivo["empleados"])]
        for i in empleados:
            empresa.ingresarEmpleado(gerente,i)
        gerente.CrearProyecto(empresa,archivo["proyectos"][0]["content"]["nombre"])
    return empresa
#obtiene los parametros necesarios para armar la clase
def getargs(classdict:dict,classname:str):
    return [classdict[i] for i in inspect.getfullargspec(eval(classname).__init__).args[1::]]       
#HERENCIA
#Dueño, Gerente y Trabajador son hijos de usuario
#Obrero y Operador son hijos de Trabajador


#Creamos un dueño para la empresa
#el dueño tiene un sueldo de 0 pero tiene un patrimonio a diferencia del resto de usuarios
propietario=Dueño("Larry Living","12345678",63,1_000_000)

#El dueño crea una empresa
#solo un dueño puede crear una empresa
empresa=propietario.crearEmpresa()

#Creamos un gerente
gerente=Gerente("Juan Perez","12345678",58,1_000_000)

#solo los gerentes pueden crear proyectos
gerente.CrearProyecto(empresa,"lucho a luchin")

empresa.ingresaGerente(propietario,gerente)
#creamos un trabajador que es un operador
harry=Operador("Harry Housen","13456723",32,300_000)
#el gerente ingresa a un nuevo empleado, solo los gerentes y dueños pueden hacer esto
empresa.ingresarEmpleado(gerente,harry)

#Verificamos si el gerente puede mandar al propietario
print(gerente.PuedeMandar(propietario))

#creamos un obrero
nuevo_obrero=Obrero("Pepe Papero","12345623",30,400_000)

#creamos un operador
nuevo_operador=Operador("Pipo Pimiro","12345678",24,400_000)
#si harry intenta ingresar un empleado no podra
try:
    empresa.ingresarEmpleado(harry,nuevo_obrero)
except NoPrivilegeError:
    #el dueño ingresa al nuevo empleado
    empresa.ingresarEmpleado(propietario,nuevo_obrero)
    empresa
finally:
    print("el dueño ingreso al empleado")

#el gerente puede cambiar el sueldo de los trabajadores
gerente.CambiarSueldo(empresa.empleados[0],400_000)

try:
    nuevo_operador.marcar_entrada(empresa,nuevo_operador.password)
except NoPrivilegeError:
    print(f"{nuevo_operador.nombre_usuario} no es un trabajador en esta empresa")
finally:
    empresa.ingresarEmpleado(gerente,nuevo_operador)
    empresa.empleados[-1].marcar_entrada(empresa,nuevo_operador.password)

        
print(propietario.password)
#Para permanencia de datos, se puede convertir en un archivo json, similar a un archivo en un sistema noSQL
#los datos quedaron cargados con anterioridad por lo que no es necesario correr extract
#si cargan desde los datos obtendran los mismos resultados que los generados en ejecución
#extract(empresa)
empresa_load=load()
pprint(empresa.__dict__)
pprint(empresa_load.__dict__)


#Comprobamos que los datos son los mismos
#Las contraseñas pueden ser distintas porque no se consideraron para el ejemplo
print(empresa.__dict__==empresa_load.__dict__)
