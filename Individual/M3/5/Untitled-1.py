from pprint import pprint
from datetime import datetime
from faker import Faker
import random 

fake = Faker()
fecha_referencia = datetime(2024, 2, 28)


usuarios = [
    {
        "identificacion": "CV001",
        "nombre_usuario": fake.user_name(),
        "antiguedad": (fecha_referencia - datetime(2021, 5, 10)).days,
        "fecha_incorporacion": datetime(2021, 5, 10),
        "informacion_personal": {
            "nombre": fake.name(),
            "edad": fake.random_int(min=18, max=80),
            "genero": random.choice(["Masculino", "Femenino", "No binario"])
        }
    },
    {
        "identificacion": "CV002",
        "nombre_usuario": fake.user_name(),
        "antiguedad": (fecha_referencia - datetime(2023, 2, 15)).days,
        "fecha_incorporacion": datetime(2023, 2, 15),
        "informacion_personal": {
            "nombre": fake.name(),
            "edad": fake.random_int(min=18, max=80),
            "genero": random.choice(["Masculino", "Femenino", "No binario"])
        }
    },
    {
        "identificacion": "CV003",
        "nombre_usuario": fake.user_name(),
        "antiguedad": (fecha_referencia - datetime(2022, 8, 20)).days,
        "fecha_incorporacion": datetime(2022, 8, 20),
        "informacion_personal": {
            "nombre": fake.name(),
            "edad": fake.random_int(min=18, max=80),
            "genero": random.choice(["Masculino", "Femenino", "No binario"])
        }
    },
    {
        "identificacion": "CV004",
        "nombre_usuario": fake.user_name(),
        "antiguedad": (fecha_referencia - datetime(2020, 11, 5)).days,
        "fecha_incorporacion": datetime(2020, 11, 5),
        "informacion_personal": {
            "nombre": fake.name(),
            "edad": fake.random_int(min=18, max=80),
            "genero": random.choice(["Masculino", "Femenino", "No binario"])
        }
    },
    {
        "identificacion": "CV005",
        "nombre_usuario": fake.user_name(),
        "antiguedad": (fecha_referencia - datetime(2019, 7, 30)).days,
        "fecha_incorporacion": datetime(2019, 7, 30),
        "informacion_personal": {
            "nombre": fake.name(),
            "edad": fake.random_int(min=18, max=80),
            "genero": random.choice(["Masculino", "Femenino", "No binario"])
        }
    },
    {
        "identificacion": "CV006",
        "nombre_usuario": fake.user_name(),
        "antiguedad": (fecha_referencia - datetime(2022, 3, 8)).days,
        "fecha_incorporacion": datetime(2022, 3, 8),
        "informacion_personal": {
            "nombre": fake.name(),
            "edad": fake.random_int(min=18, max=80),
            "genero": random.choice(["Masculino", "Femenino", "No binario"])
        }
    }
]

pprint(usuarios)