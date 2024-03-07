
LOG=[]
def registro(func):
    def new_func(*args,**kwargs):
        LOG.append(func.__name__)
        func
    return new_func
@registro
def suma(a,b):
    return a+b
@registro
def resta(a,b):
    return a-b
@registro
def prod(a,b):
    return a*b
@registro
def diff(a,b):
    if b==0:
        return None
    return a/b
def filtrar(*args,**kwargs):
    def inner(func):
        def new_fuction():
            password=input("ingrese contraseña: ")
            if (password==args[0]):
                print("correcto")
                return func()
            return "Contraseña no valida"
        return new_fuction
    return inner
@filtrar("12345")
def imprimirHola():
    print("hola")
resta(1,2)
suma(1,2)
prod(1,3)
diff(1,4)
suma(1,2)
print(LOG)

imprimirHola()