from django.db import models


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=True)
class Brand(models.Model):
    name=models.CharField(max_length=100,null=True)
class ProductType(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
class Warrant(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
class ProductImages(models.Model):
    img=models.ImageField()
class Product(models.Model):
    sku=models.IntegerField(unique=True),
    name=models.CharField(max_length=100,null=True)
    spects=models.TextField(blank=True)
    price=models.IntegerField(blank=False,default=0)
    warrant=models.ManyToManyField(Warrant)
    pictures=models.ManyToManyField(ProductImages)
