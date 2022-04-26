from django.db import models
from products.models import Product
from users.models import User

class Order(models.Model):
    user_id    = models.ForeignKey(User,    on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    qunatity   = models.IntegerField()
    price      = models.DecimalField()
    status     = models.CharField(max_length=30)

    class Meta:
        db_table = 'orders'

class Cart(models.Model):
    user_id    = models.ForeignKey(User,    on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qunatity   = models.IntegerField()
    price      = models.DecimalField()

    class Meta:
        db_table = 'carts'