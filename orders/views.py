from ast import Or
from curses.ascii import US
import json
from unicodedata import decimal

from orders.models   import Order, Cart, Status 
from products.models import Product
from users.models    import User
from django.http     import JsonResponse
from django.views    import View
from core.decorator  import log_in_decorator
from json.decoder    import JSONDecodeError

class CartView(View):
    @log_in_decorator
    def post(self,request):
        try : 
            carts = Cart.objects.filter(user_id = request.user.id)
            result = []
            for cart in carts:
                product = Product.objects.get(id = cart.product_id)
                result.append(
                 {
                        "cart_id" : cart.id,
                        "product"  : product.name,
                        "produtc_image_1" : product.thumnail_url_1,
                        "produtc_image_2" : product.thumnail_url_2,
                        "price" : cart.price,
                        "quantity" : cart.quantity,
                    }
                )
            return JsonResponse({'carts' : result}, status=200)
        except KeyError:
            return JsonResponse('KeyError',status = 401)   
        
class CartCreateView(View):
    @log_in_decorator
    def post(self,request):
        try : 
            user_id = request.user.id
            data = json.loads(request.body)
            quantity = data['quantity']
            price    = data['price'] 
            Cart.objects.create(   
                quantity = quantity,
                price    = price,
                product_id = data['product_id'],
                user_id = user_id
            )
            return JsonResponse({'message': 'cart created'}, status=201)
        except KeyError:
            return JsonResponse('KeyError',status = 401)    
        except JSONDecodeError:
            return JsonResponse({'message':'json형태이상함'},status=400)
            
class CartDeleteView(View):
    def delete(self,request):
        try:
            #user        = request.user
            data        = json.loads(request.body)
            cart        = Cart.objects.get(id=data['cart_id'])

            Cart.objects.filter(id=cart.id).delete()
            return JsonResponse({'mesaage':'삭제완료'},status=200)
        except KeyError:
            return JsonResponse({'message':'키에러'},status=400)
        except Order.DoesNotExist:
            return JsonResponse({'message':'삭제할 장바구니가 존재하지 않습니다.'},status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'json형태이상함'},status=400)
            
class OrderView(View):
    @log_in_decorator
    def post(self,request):
        try : 
            orders = Order.objects.filter(user_id = request.user.id)
            result = []
            for order in orders:
                product = Product.objects.get(id = order.product_id)
                status  = Status.objects.get(id = order.status_id)
                result.append(
                    {
                        "order_id" : order.id,
                        "product"  : product.name,
                        "produtc_image_1" : product.thumnail_url_1,
                        "produtc_image_2" : product.thumnail_url_2,
                        "price" : order.price,
                        "quantity" : order.quantity,
                        "status" : status.status
                    }
                )
            return JsonResponse({'orders' : result}, status=200)
        except KeyError:
            return JsonResponse('KeyError',status = 401)    

class OrderCreateView(View):
    @log_in_decorator
    def post(self,request):
        try : 
            data = json.loads(request.body)
            carts = list(data['cart_id'])
            for i in carts :
                cart = Cart.objects.get(id = i)
                Order.objects.create(
                    quantity = cart.quantity,
                    price = cart.price,
                    product_id = cart.product_id,
                    user_id = cart.user_id,
                    status_id = 2
                )
                Cart.objects.filter(id = i).delete()
            return JsonResponse({'message' : 'order created'}, status=201)
        except KeyError:
            return JsonResponse({'message':'키에러'},status=400)
        except Cart.DoesNotExist:
            return JsonResponse({'message':'삭제할 장바구니가 존재하지 않습니다.'},status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'json형태이상함'},status=400)
