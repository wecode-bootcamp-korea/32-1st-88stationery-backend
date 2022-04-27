from django.db       import models
from products.models import Product
from users.models    import User

class Status(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        db_table = 'statuses'

class Order(models.Model):
    user     = models.ForeignKey(User,    on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price    = models.DecimalField(max_digits=10, decimal_places=2)
    status   = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'

class Cart(models.Model):
    user     = models.ForeignKey(User,    on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price    = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'carts'