from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    edad=models.IntegerField(null=False,blank=False,default=12)
    nombre_usuario=models.CharField(max_length=255)
    contraseña=models.CharField(max_length=255)