import re
def filtrar(*args,**kwargs):
    def inner(func):
        def new_fuction(str):
            str=re.sub(args[0],"",str)
            return func(str)
        return new_fuction
    return inner
@filtrar(r'[^a-zA-ZáéíóúÁÉÍÓÚüÜ]')
def palindrome(str):
    if len(str)<=1:
         return True
    if str[0]==str[-1]:
        return palindrome(str[1:-1])
    else:
        return False
print(palindrome("aannaa."))