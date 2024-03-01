def prod(m1,m2):
    return sum([m1[i]*m2[i] for i in range(0,len(m1))])
def prodsumless(m1,m2):
    prod=0
    for i in range(0,len(m1)):
        prod+=m1[i]*m2[i]
    return prod

def matrix_mul(m1,m2):
    result=[]
    for i in m1:
        row_result=[]
        for j in range(0,len(i)):
            row=prod(i,[k[j] for k in m2])
            row_result.append(row)
        result.append(row_result)
    return result
matrix=((1,2,3),(-1,0,2))
producto_escalar=prod(matrix[0],matrix[1])
print(f"1. producto escalar: {producto_escalar}")
matrix1=((5,2,1),(2,1,2),(4,1,3))
matrix2=((1,4,2),(0,3,0),(2,1,3))
print(f"2. Multiplicación de matrises: \n {matrix_mul(matrix1,matrix2)}")
