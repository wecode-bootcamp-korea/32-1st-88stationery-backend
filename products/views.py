from products.models import Category, Product
from django.http     import JsonResponse
from django.views    import View

class ProductView(View):
    def get(self, request):
        order_method = int(request.GET.get('sort_method', 0))
        limit        = int(request.GET.get('limit', 8))
        offset       = int(request.GET.get('offset', 0))
        
        if order_method   == 0:
            products = Product.objects.all()[offset:offset+limit]
        elif order_method == 1:
            products = Product.objects.order_by('price')[offset:offset+limit]
        elif order_method == 2:
            products = Product.objects.order_by('-price')[offset:offset+limit]
        elif order_method == 3:
            products = Product.objects.filter(is_new = True)[offset:offset*limit]

        result = []

        for product in products:
            result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "is_new" : product.is_new,
                    "product_id" : product.id
                }
            )
        return JsonResponse({'products' : result}, status = 200)

class CategoryView(View):
    def get(self, request, category_id):
        result         = []
        product_result = []
        order_method   = int(request.GET.get('sort_method', 0))
        limit          = int(request.GET.get('limit', 8))
        offset         = int(request.GET.get('offset', 0))
        if category_id == 6 : 
            old_products = Product.objects.all()
            category     = Category.objects.get(id = category_id)
        else : 
            old_products = Product.objects.filter(category_id = category_id)
            category = Category.objects.get(id = category_id)

        if order_method   == 0:
            products = old_products[offset:offset+limit]
        elif order_method == 1:
            products = old_products.order_by('price')[offset:offset+limit]
        elif order_method == 2:
            products = old_products.order_by('-price')[offset:offset+limit]
        elif order_method == 3:
            products = old_products.filter(is_new = True)[offset:offset+limit]
        
        result.append(
            {
                "category_detail" : category.detail,
                "category_name"   : category.name
            }
        )

        for product in products:
            product_result.append(
                {
                    "name" : product.name,
                    "thumnail_url_1" : product.thumnail_url_1,
                    "thumnail_url_2" : product.thumnail_url_2,
                    "price" : product.price,
                    "is_new" : product.is_new,
                    "product_id" : product.id
                }
            )
        return JsonResponse({'category' : result, 'products' : product_result}, status = 200) 

class DetailView(View):
    def get(self, request, product_id):
        result     = []
        product   = Product.objects.filter(id = product_id)
        result.append({
                "name" : product.name,
                "thumnail_url_1" : product.thumnail_url_1,
                "thumnail_url_2" : product.thumnail_url_2,
                "price" : product.price,
                "detail" : product.detail,
                "detail_image_url" : product.detail_image_url,
                "is_new" : product.is_new,
                "product_id" : product.id
            })
        return JsonResponse({'product' : result}, status = 200) 