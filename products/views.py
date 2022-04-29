from django.shortcuts import render

# Create your views here.

import json
from unicodedata import category

from products.models import Category, Product
from django.http     import HttpResponse, JsonResponse
from django.views    import View
# from django.core import serializers
# from django.http import JsonResponse

class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        result   = []
        for product in products:
            result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "is_new" : product.is_new
                }
            )
        
        return JsonResponse({'products' : result}, status=200)

class CategoryView(View):
    def post(self, request):
        data        = json.loads(request.body)
        result      = []
        category    = Category.objects.get(name = data['name'])
        category_id = category.id
        products    = Product.objects.filter(category_id = category_id)

        for product in products:
            result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "category_detail" : category.detail,
                    "category_name"   : category.name
                }
            )

        return JsonResponse({'products' : result}, status=200) 

class DetailView(View):
    def post(self, request):
        data       = json.loads(request.body)
        result     = []
        product_id = Product.objects.get(name = data['name']).id
        products   = Product.objects.filter(id = product_id)

        for product in products:
            result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "detail" : product.detail,
                    "detail_image_url" : product.detail_image_url,
                    "is_new" : product.is_new
                }
            )

        return JsonResponse({'products' : result}, status=200) 