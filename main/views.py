import json

from products.models import Product
from django.http     import JsonResponse
from django.views    import View

class MainView(View):
    def get(self, request):
        limit        = int(request.GET.get('limit', 8))
        new_limit    = int(request.GET.get('new_limit'),4)
        offset       = int(request.GET.get('offset', 0))
        products     = Product.objects.all()[offset:offset+limit]
        new_products = Product.objects.filter(is_new = True)[offset:offset+new_limit]
        new_result   = []
        result       = []

        for product in new_products:
            new_result.append({
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "product_id" : product.id
                })

        for product in products:
            result.append({
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "product_id" : product.id
                })
        return JsonResponse({'new_products' : new_result, 'products' : result}, status = 200)