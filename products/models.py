from django.db import models

class Category(models.Model):
    name   = models.CharField(max_length=45)
    detail = models.CharField(max_length=300,null=True)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name             = models.CharField(max_length=45)
    price            = models.DecimalField(max_digits=10, decimal_places=2)
    thumnail_url_1   = models.CharField(max_length=500)
    thumnail_url_2   = models.CharField(max_length=500,null=True)
    detail           = models.TextField(default='Detail')
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    is_new           = models.BooleanField(default=False)
    is_best          = models.BooleanField(default=False)           
    category         = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'products'
