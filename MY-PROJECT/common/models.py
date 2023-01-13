from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    phone =models.BigIntegerField()
    address = models.CharField(max_length=60)   #default = ''  if we add new field add this
 
    class Meta:
        db_table = 'customer_tb'

class Seller(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    user_name =  models.IntegerField(default=0)
    phone =models.BigIntegerField()
    address = models.CharField(max_length=60)
    bank_name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=10)
    account_no = models.CharField(max_length=15)
    seller_pic = models.ImageField(upload_to= 'seller/')
    class Meta:
        db_table = 'seller_tb'




