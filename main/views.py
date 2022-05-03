import json

from products.models import Product
from django.http     import JsonResponse
from django.views    import View

class MainView(View):
    def get(self, request):
        limit        = int(request.GET.get('limit', 6))
        offset       = int(request.GET.get('offset', 0))
        new_products = Product.objects.filter(is_new = True)[offset:offset+limit]
        result       = []

        for product in new_products:
            result.append({
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "product_id" : product.id
                })

        return JsonResponse({'new_products' : result}, status = 200)