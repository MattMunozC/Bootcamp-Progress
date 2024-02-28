def fib(n):
    if (n<2):
        return n
    else:
        return fib(n-1)+fib(n-2)
def fib2(n):
    values=[0,1]
    if (n<2):
        return values[n]
    else:
        print(*values, end=" ")
        for _ in range(0,n):
            pivot=values[0]
            values[0]=values[1]
            values[1]=values[0]+pivot
            print(values[1],end=" ")
        return values[1]
def fib3(n):
    n = 10

    num1 = 0

    num2 = 1

    next_number = num2  

    count = 1
    

    while count <= n:

        print(next_number, end=" ")

        count += 1

        num1, num2 = num2, next_number

        next_number = num1 + num2

    print()
fib2(10)