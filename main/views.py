import json

from products.models import Product
from django.http     import JsonResponse
from django.views    import View

class MainView(View):
    def get(self, request):
        new_products = Product.objects.filter(is_new=True)
        products     = Product.objects.all()
        new_result = []
        result =[]
        for product in new_products:
            new_result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price
                }
            )
        for product in products:
            result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price
                }
            )
        return JsonResponse({'new_products' : new_result, 'products' : result}, status=200)