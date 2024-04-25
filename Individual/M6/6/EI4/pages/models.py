from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class usuario(AbstractUser):
    age=models.IntegerField(null=False,blank=False,default=0)
    REQUIRED_FIELDS=['password','email','age']
    def check_password(self, raw_password: str) -> bool:
        return self.password==raw_password