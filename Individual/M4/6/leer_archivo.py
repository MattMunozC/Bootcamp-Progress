class Data():
    def __init__(self):
        self.data=[]
        with open("datos.csv","r",encoding="UTF-8") as datos:
            for enum,i in enumerate(datos.read().split("\n")[1::]):
                row=i.split(",")
                row[1]=row[1][1::]
                row[2]=row[2][1::]
                if Data.validate_phone(row[1]) and row[2].isdigit():
                    self.data.append(dict(zip(["nombre","telefono","edad"],row)))
                else:
                    print(f"Dato invalido en linea {enum}")
    @staticmethod
    def validate_phone(phonenumber:str)->bool:
        if len(phonenumber)!=8:
            return False
        if not phonenumber.isdigit():
            return False
        return True