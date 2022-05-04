from django.shortcuts import render
from products.models  import Product, Category
from django.http      import JsonResponse
from django.views     import View

class SearchView(View):
    def get(self, request):
        limit         = int(request.GET.get('limit', 4))
        offset        = int(request.GET.get('offset', 0))
        search_word   = str(request.GET.get('search'))
        searched_products  = Product.objects.filter(name__icontains=search_word).distinct()[offset:offset+limit]
        result = []

        for product in searched_products:
            result.append({
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "product_id" : product.id
                })

        return JsonResponse({'searched_products' : result}, status = 200)
