from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name             = models.CharField(max_length=45)
    price            = models.DecimalField(max_digits=10, decimal_places=2)
    thumnail_url     = models.CharField(max_length=500)
    detail           = models.TextField()
    detail_image_url = models.CharField(max_length=500)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    new_product      = models.BooleanField()           
    category         = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'products'
