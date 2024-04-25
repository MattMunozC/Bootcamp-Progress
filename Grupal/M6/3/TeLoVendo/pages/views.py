from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(requests):
    return render(requests,"index.html")
def list_clients(request):
    return render(request,'client.html',context={"clients":[
        {
            "Nombre":"juaquin Juan",
            "Apellido":"Harry",
            "Correo":"Lacayodetulio@gmail.com",
            "Ciudad_natal":"Titirilquen",
            "Tier":"Oro",
            "Registrado_en":"2 de octubre 2001",
            "Deuda":False
         },
         {
            "Nombre":"Tulio",
            "Apellido":"Triviño",
            "Correo":"elMejorReportero@gmail.com",
            "Ciudad_natal":"San Rosendo",
            "Tier":"Platino",
            "Registrado_en":"14 de Junio 2000",
            "Deuda":False
          },
          {
              "Nombre":"Juan Carlos",
              "Apellido":"Bodoque",
              "Correo":"TormentaChinaEnjoyer@gmail.com",
              "Ciudad_natal":"Titiritalca",
              "Tier":"Bronce",
              "Registrado_en":"15 de marzo de 2003",
              "Deuda":True
          },
          {
              "Nombre":"Patria Ana",
              "Apellido":"Tufillo",
              "Correo":"laSombra@gmail.com",
              "Ciudad_natal":"Titirilquen",
              "Tier":"Plata",
              "Registrado_en":"31 de mayo de 2003",
              "Deuda":False
          },
          {
              "Nombre":"Policarpo",
              "Apellido":"Avedaño",
              "Correo":"Toptoptoptoptop@gmail.com",
              "Ciudad_natal":"Titiricauquenes",
              "Tier":"Oro",
              "Registrado_en":"15 de marzo de 2003",
              "Deuda":False
          }
        ]
        })