from django.db import models

# Create your models here

class UserData(models.Model):  #class Model is called from models (check package)
    username = models.CharField(max_length= 100)
    phone_no = models.BigIntegerField()
    dob = models.DateField()
    email = models.CharField(max_length= 100)
    pswd = models.CharField(max_length= 100)


class ProductDetails(models.Model):
    serial_no= models.CharField(max_length = 100)
    product_name = models.CharField(max_length = 100)
    model_name = models.CharField(max_length = 100)
    seller_name = models.CharField(max_length = 100)
    stock_num = models.BigIntegerField()
    ratings = models.BigIntegerField()
    price = models.BigIntegerField()
