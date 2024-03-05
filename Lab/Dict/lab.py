import re
from pprint import pprint
ARTICULOS=["","es","son","con","las","para","esta","sea","si","vez","era","también","cuando""han","ha","hasta","será","os","tanto","pero","o","entre","cada","este","somos","nos","le","mí","ni","mis","desde","tu","no","lo","que","su","a","así","por","eso","les","sus","y","como","ya","acá","el","la","de","un","una","porque","que","se","en","al","del","los","más","ma","mi","nui","pun","may"]
def filtrar(str,filtro=r'[^a-zA-ZáéíóúÁÉÍÓÚüÜ]'):
    return re.sub(filtro,";",str)
def contar(contenido,count):
    dc={i:contenido.count(i) for i in contenido if i.lower() not in ARTICULOS}
    sortdc=sorted(dc.items(), key=lambda x:x[1])[:count*-1:-1]
    return [i[0] for i in sortdc]
def findNum(ls):
    for num,i in enumerate(ls):
        if i.isdigit():
            return num
with open("discurso_boric.txt","r",encoding="UTF-8") as archivo:
    contenido=filtrar(archivo.read()).split(";")
    boric=contar(contenido,50)
with open("discurso_milei.txt","r",encoding="UTF-8") as archivo:
    contenido=filtrar(archivo.read()).split(";")
    milei=contar(contenido,50)
print("palabras más dichas por boric:")
pprint(boric)
print("palabras más dichas por milei:")
pprint(milei)
valores_2021 = {
    'dolar': 974.38,
    'euro': 1057.54,
    'reales brasilenos': 196.98,
    'rublos': 10.65
}

peso_chileno=input("Ingrese un monto(CLP): ")
while not peso_chileno.isdigit():
    peso_chileno=input("Ingrese un monto correcto(CLP): ")
for i in valores_2021:
    print(f"{peso_chileno} CLP en {i} es igual a {'{:.2f}'.format(float(peso_chileno)/valores_2021[i])}")
try:
    with open("alumnos.txt","r",encoding="UTF-8") as archivo:
        contenido=[i for i in archivo.read().split("\n")]
        CRUD={}
        for i in contenido:
            i=i.split(" ")
            CRUD[i[0]]={"nombre":i[1],"apellido":i[2],"dirección":' '.join(i[3:findNum(i)+1]),"región":" ".join(i[i.index("Región")::])}
        pprint(CRUD)
except:
    print("el archivo se encuentra vacio o no existe")