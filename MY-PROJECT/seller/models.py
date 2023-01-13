from django.db import models
from common.models import Seller

# Create your models here.


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE) 
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    product_no= models.BigIntegerField()
    product_description = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    stock = models.IntegerField()
    image = models.ImageField(upload_to= 'product/')
    class Meta:
        db_table = 'product_tb'


