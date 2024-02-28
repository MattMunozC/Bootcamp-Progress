#Parte 1
import re
import random
import time
from pprint import pprint

mayusucula=".*[A-Z].*"
numeros=".*[0-9].*"
minuscula=".*[a-z].*"
isOK=False
while not isOK:
    clave=input("Ingrese una contraseña: ")
    #Todo en orden
    isOK=True
    #Si se cumple cualquiera de los if entonces ya no esta en orden
    if not bool(re.search(mayusucula,clave)):
        print("*La contraseña debe contener al menos una mayuscula")
        isOK=False
    if not bool(re.search(minuscula,clave)):
        print("*La contraseña debe contener al menos una minuscula")
        isOK=False
    if not bool(re.search(numeros,clave)):
        print("*La contraseña debe contener al menos un numero")
        isOK=False
    if len(clave)<8:
        print("*La contraseña debe contener un minimo de 8 caracteres")
        isOk=False

#Parte 2
nombres = ["Ana", "Juan", "María", "Carlos", "Laura", "Pedro", "Sofía"]
        
Cuestionarios=['Hábitos alimenticios', 'experiencia laboral', 'actividades recreativas', 'atletismo', 'natación', 'deportes en general']


envios={i:{"total":0,"Cuestionarios a contestar": []} for i in nombres}

Cuestionarios_a_enviar=100

Cuestionarios_enviados=0

if Cuestionarios_a_enviar>len(nombres)*5:
    Cuestionarios_a_enviar=len(nombres)*5

while Cuestionarios_enviados<Cuestionarios_a_enviar:
    time.sleep(3)
    persona_seleccionada=random.randint(0,len(nombres)-1)
    persona=nombres[persona_seleccionada]
    if (envios[persona]["total"])<5:
        Cuestionario_seleccionado=random.randint(0,len(Cuestionarios)-1)
        cuestionario=Cuestionarios[Cuestionario_seleccionado]
        envios[persona]["Cuestionarios a contestar"].append(cuestionario)
        envios[persona]["total"]=len(envios[persona]["Cuestionarios a contestar"])
        print(f"Enviando cuestionario '{cuestionario}' a {persona}")
        Cuestionarios_enviados+=1

pprint(envios)