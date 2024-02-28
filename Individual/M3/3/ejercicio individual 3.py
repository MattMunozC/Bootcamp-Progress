BINARY_TRANSFORM={"S":True,"N":False}
edad=input("Edad: ")
while not edad.isdigit():
    edad=input("Edad: ")
edad=int(edad)
nacionalidad=input("¿es usted latino americano?(S/N) ")
while nacionalidad.lower() not in ("s","n"):
    nacionalidad=input("¿es usted latino americano?(S/N) ")
afinidad=input("¿Tiene afinidad por los deportes?(S/N) ")
while afinidad.lower() not in ("s","n"):
    afinidad=input("¿es usted latino americano?(S/N) ")
cuestionarios=[]
if edad>=18 and edad<=29:
    cuestionarios.append("empleabilidad")
elif edad>=30 and edad<=59 and BINARY_TRANSFORM[nacionalidad.upper()]:
    cuestionarios.append("experiencia laboral")
elif edad>=60 and BINARY_TRANSFORM[nacionalidad.upper()]:
    cuestionarios.append("actividades recreativas")
if BINARY_TRANSFORM[afinidad.upper()] and edad<=60:
    cuestionarios.append("atletismos")
elif BINARY_TRANSFORM[afinidad.upper()] and edad>60:
    cuestionarios.append("natacion")
if not BINARY_TRANSFORM[afinidad.upper()]:
    cuestionarios.append("Deporte General")
print(f"cuestionarios a contestar: {len(cuestionarios)} \ntotal: {cuestionarios}")
    