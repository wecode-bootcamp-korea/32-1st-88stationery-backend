from django.db import models
from users.models import User
from orders.models import Order, Cart

class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name             = models.CharField(max_length=45)
    price            = models.DecimalField()
    thumnail_url     = models.CharField(max_length=500)
    detail           = models.CharField(max_length=10000)
    detail_image_url = models.CharField(max_length=500)
    created_at       = models.DateTimeField(auto_now_add=True)
    new_product      = models.BooleanField()           
    category         = models.ForeignKey(Category, on_delete=models.CASCADE)
    order            = models.ManyToManyField(User, through="Order")
    cart             = models.ManyToManyField(User, through="Cart")
    
    class Meta:
        db_table = 'products'
