from django.urls import path
from orders.views import CartDeleteView, OrderView, OrderCreateView , CartView, CartCreateView

urlpatterns = [
    path('', OrderView.as_view()),
    path('/create', OrderCreateView.as_view()),
    path('/cart', CartView.as_view()),
    path('/cart/create', CartCreateView.as_view()),
    path('/cart/delete', CartDeleteView.as_view())
]