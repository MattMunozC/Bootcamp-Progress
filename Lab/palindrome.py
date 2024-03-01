import re
def filtrar(str,filtro):
    return re.sub(filtro,"",str)
def palindromo(str):
#filtrar caracteres invalidos
    str=filtrar(str,r'[^a-zA-ZáéíóúÁÉÍÓÚüÜ]')
    str_len=len(str)
    reversed_str=""
#invertir palabra
    for i in range(str_len-1,-1,-1):
        reversed_str+=str[i]
    return str==reversed_str
palabra=input("frase: ")
print(f"es la palabra {palabra} un palindromo? {palindromo(palabra)}")