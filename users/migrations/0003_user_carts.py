# Generated by Django 4.0.4 on 2022-04-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0002_user_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='carts',
            field=models.ManyToManyField(related_name='user_cart', through='orders.Cart', to='products.product'),
        ),
    ]
