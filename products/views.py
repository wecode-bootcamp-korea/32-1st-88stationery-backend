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
        result = []
        for product in products:
            result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price
                }
            )
        
        return JsonResponse({'products' : result}, status=200)

class CategoryView(View):
    def get(self, request):
        data = json.loads(request.body)
        category_id = Category.objects.get(name = data['name']).id
        products = Product.objects.filter(category_id = category_id).values('id','name','thumnail_url_1','thumnail_url_2','price')
        return HttpResponse(products,content_type="text/html",status=200)

class DetailView(View):
    def get(self, request):
        data = json.loads(request.body)
        product_id = Product.objects.get(name = data['name']).id
        product    = Product.objects.filter(id = product_id).values('id','name','thumnail_url_1','thumnail_url_2','price','detail','detail_image_url','is_new')
        return HttpResponse(product, content_type="text/html", status=200)