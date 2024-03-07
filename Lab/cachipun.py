import random
def juez(jugador,cpu):
    numval={"piedra":1,"papel":2,"tijera":3}
    if numval[jugador]==1 and numval[cpu]==3:
        return "victoria"
    elif numval[jugador]==numval[cpu]:
        return "Empate"
    else:
        return "victoria" if numval[jugador]>numval[cpu] else "derrota"

while 1:
    jugador=input("piedra, papel, tijera:")
    cpu=random.choice(["piedra","papel","tijera"])
    if jugador=="salir":
        break
    print(f"cpu juega {cpu}: {juez(jugador,cpu)}")