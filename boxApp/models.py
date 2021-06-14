from django.db import models


# Create your models here.
class ProductType(models.Model):
    type_id = models.CharField(primary_key=True, max_length=50)
    value = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Product(models.Model):
    model = models.CharField(primary_key=True, max_length=50)
    maker = models.CharField(max_length=50)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)


class PC(models.Model):
    code = models.IntegerField(primary_key = True)
    speed = models.IntegerField()
    hd = models.FloatField()
    ram = models.IntegerField()
    cd = models.CharField(max_length= 20)
    price = models.FloatField()
    model = models.ForeignKey(Product, on_delete= models.CASCADE)
