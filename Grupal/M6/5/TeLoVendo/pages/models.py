from django.db import models
from django.contrib.auth.models import AbstractUser

class Tier(models.Model):
    name=models.CharField(max_length=255)

# Create your models here.
class Client(AbstractUser):
    REQUIRED_FIELDS=["password"]
    birthplace=models.CharField(max_length=255)
    tier=models.ForeignKey(Tier,on_delete=models.CASCADE)
    total_spend=models.IntegerField(null=False,default=0)
    debt=models.BooleanField(null=False,default=False,blank=True,help_text="whether the client has debts or not")
    def check_password(self, raw_password: str) -> bool:
        return self.password==raw_password

class Category(models.Model):
    name=models.CharField(max_length=100)
class Collaborator(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
