from django.db import models
from products.models import Product
from orders.models import Order, Cart

class User(models.Model):
    email        = models.CharField(max_length=100,unique=True)
    password     = models.CharField(max_length=100)
    name         = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    birth_date   = models.CharField(max_length=10)
    address1     = models.CharField(max_length=50)
    address2     = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
