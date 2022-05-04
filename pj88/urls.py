from django.urls import path, include

urlpatterns = [
    path('users',include('users.urls')),
    path('products', include('products.urls')),
    path('main', include('main.urls')),
    path('orders', include('orders.urls')),
    path('questions',include('questions.urls'))
]
