import re
from paquete import modulo
from paquete.modulo import resta

#mensaje motivador I
frase="¡Matías, Eduardo, Sebastián y Daniel! Ustedes son los arquitectos de sus propios éxitos. Con determinación y perseverancia, cada paso que den los llevará más cerca de alcanzar sus metas. Recuerden que cada desafío es una oportunidad para crecer y aprender. ¡Confíen en ustedes mismos y sigan adelante con pasión y determinación! El camino hacia el éxito está lleno de obstáculos, pero también de innumerables oportunidades para brillar. ¡Vamos con todo!"

#Todo el mensaje ahora esta en mayuscula II
frase=frase.upper()

#se divide en una lista de palabras III
lista=re.sub(r'[^a-zA-Z áéíóúÁÉÍÓÚüÜ]',"",frase).split(" ")

#cantidad de palabras en el string V
len_frase=len(lista)

#tupla de palabras VI
print(tuple(lista))

#ingrese otro mensaje por teclado VII
input("Ingrese otro mensaje")
