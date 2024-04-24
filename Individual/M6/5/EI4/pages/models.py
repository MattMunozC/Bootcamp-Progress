from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class usuario(AbstractUser):
    USERNAME_FIELD='nombre_usuario'
    PASSWORD_FIELD="contraseña"
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    edad=models.IntegerField(null=False,blank=False,default=12)
    nombre_usuario=models.CharField(max_length=255,unique=True)
    contraseña=models.CharField(max_length=255)
    def check_password(self, raw_password: str) -> bool:
        return self.contraseña==raw_password