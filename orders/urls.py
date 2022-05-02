from django.urls import path
from orders.views import CartDeleteView, OrderView, OrderCreateView , CartView, CartCreateView

urlpatterns = [
    path('', OrderView.as_view()),
    path('/cart', CartView.as_view()),
]
