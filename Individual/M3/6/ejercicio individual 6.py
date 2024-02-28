from time import sleep
from getpass import getpass
datos_recolectados={}
opciones=["salir","registrarme"]
print("Bienvenido,",end=" ")
while 1:
    if len(datos_recolectados)==0:
        print("por favor seleccione una de las siguientes opciones para continuar\n")
    else:
        print("usuarios registrados:")
        for i in datos_recolectados:
            print(i)
            print(f"\tNombre de usuario: {i} \n\tcontraseña: {datos_recolectados[i]["contraseña"]} \n\tedad: {datos_recolectados[i]["edad"]}\n\n\n")
            sleep(5)
        print("Hola de nuevo, por favor seleccione una accion")
    print("\t*si desea inscribirse como usuario escriba 'registrarme'\n\t*si desea salir escriba 'salir'")
    seleccion=input("escriba su eleccion: ")
    if seleccion not in opciones:
        continue
    else:
        if seleccion==opciones[0]:
            break
        elif seleccion==opciones[1]:
            print("Nos alegra que te nos unas")
            username=input("Nombre de Usuario: ")
            while username in datos_recolectados.keys():
                username=input(f"{"*"*5}Nombre de usuario no disponible{"*"*5}\nNombre de Usuario: ")
            password=getpass("Ingrese una contraseña: ")
            edad=input("Ingrese su edad: ")
            while not edad.isdigit():
                edad=input("Ingrese una edad valida: ")
            datos_recolectados[username]={
                    "contraseña":password,
                    "edad":edad
                    }
print("Hasta pronto")