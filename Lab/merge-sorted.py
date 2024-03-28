

list1=[1,2,4]
list2=[1,3,5]
pivot=0
for element in list2:

    while 1:
        if list1[pivot]<=element:
            print(pivot)
            list1.insert(pivot,element)
            pivot=pivot+1
            break
        pivot+=1
print(list1)