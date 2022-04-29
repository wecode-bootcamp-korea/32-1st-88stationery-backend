from django.urls import path
from products.views import ProductView, CategoryView, DetailView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/category', CategoryView.as_view()),
    path('/detail', DetailView.as_view()),
]