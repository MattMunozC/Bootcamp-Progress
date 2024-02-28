factor=[1,10,2]
with open("input.txt","r") as file:
    base=[int(i) for i in file.read().split("\n")]
    for X in base:
        pol = 0
        for exp in range(0,3):
            pol = pol + factor[exp] * pow(X ,exp)
            print(exp,pow(X ,exp),factor[exp])
        print("Valor : " + str(X) + " polinomio : " + str(pol))