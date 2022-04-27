from django.db       import models

class User(models.Model):
    email        = models.CharField(max_length=100,unique=True)
    password     = models.CharField(max_length=100)
    name         = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    birth_date   = models.DateField()
    address1     = models.CharField(max_length=50)
    address2     = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    orders       = models.ManyToManyField('products.Product', through="orders.Order", related_name='user_order')
    carts        = models.ManyToManyField('products.Product', through="orders.Cart", related_name='user_cart')

    class Meta:
        db_table = 'users'
