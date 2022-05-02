from django.urls import path
from products.views import ProductView, CategoryView, DetailView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/category/<int:category_id>', CategoryView.as_view()),
    path('/detail/<int:product_id>', DetailView.as_view()),
]