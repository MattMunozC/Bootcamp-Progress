class test():
    def __init__(self,val=0):
        self.num=val
    def __add__(self,val):
        if type(val)==int:
            return self.num+val
        if type(val)==str:
            return val
        if type(val)==test:
            return self.num+val.num
if __name__=="__main__":
    a=test(4)
    print(a+2)
    print(a+"hola mundo")
    print(a+test(5))