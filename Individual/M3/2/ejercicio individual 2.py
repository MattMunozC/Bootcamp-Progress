
#String de nombres
USERS_STRING="Sofía, Mateo, Valentina, Alejandro, Isabella, Santiago, Camila"

#si se quisiera buscar un nombre dentro del string se podria utilizar String.find(substring)
USERS_STRING.find("Sofía")
USERS_STRING.find("Mateo")
USERS_STRING.find("Santiago")

#buscar dentro de un string es ineficiente y haría más lento cualquier aplicación con más usuarios
#hay que utilizar una lista
USERS=USERS_STRING.split(",")

#tambien se puede saber cuantos usuarios hay
print(len(USERS))

#se puede definir un mensaje de saludo personal para cada persona 
saludos = {
    "Sofía": "¡Hola Sofía! Espero que tu día esté lleno de alegría y aventuras.",
    "Mateo": "¡Hola Mateo! Que tengas un día lleno de éxito y oportunidades.",
    "Valentina": "¡Hola Valentina! Espero que hoy brilles tanto como siempre.",
    "Alejandro": "¡Hola Alejandro! Que hoy encuentres inspiración y motivación en todo lo que hagas.",
    "Isabella": "¡Hola Isabella! Que hoy sea tan hermoso como tú.",
    "Santiago": "¡Hola Santiago! Que el camino que recorras hoy esté lleno de buenos momentos y aprendizajes.",
    "Camila": "¡Hola Camila! Que tu día esté lleno de sonrisas y momentos especiales."
}

#y ahora solo falta llamar al elemento en la lista 

print(saludos["Sofía"]) 