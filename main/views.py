import json

from products.models import Product
from django.http     import JsonResponse
from django.views    import View

class MainView(View):
    def get(self, request):
        limit         = int(request.GET.get('limit', 4))
        offset        = int(request.GET.get('offset', 0))
        new_products  = Product.objects.filter(is_new = True)[offset:offset+limit]
        best_products = Product.objects.filter(is_best = True)[offset:offset+limit+2]
        new_result    = []
        best_result   = []

        for product in new_products:
            new_result.append({
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "product_id" : product.id
                })

        for product in best_products:
            best_result.append({
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "product_id" : product.id
                })

        return JsonResponse({'new_products' : new_result, 'best_products' : best_result}, status = 200)