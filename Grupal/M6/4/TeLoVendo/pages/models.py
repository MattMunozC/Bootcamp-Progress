from django.db import models

class Tier(models.Model):
    name=models.CharField(max_length=255)

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    birthplace=models.CharField(max_length=255)
    register_in=models.DateField(auto_now=True,help_text="Date the client register")
    tier=models.ForeignKey(Tier,on_delete=models.CASCADE)
    debt=models.BooleanField(null=False,default=False,blank=True,help_text="whether the client has debts or not")
class Category(models.Model):
    name=models.CharField(max_length=100)
class Collaborator(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
