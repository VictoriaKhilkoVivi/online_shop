from django.urls import path

from . import views

urlpatterns = [
    path('', views.categories_list, name='categories_list'),
    path('<int:id>/', views.products_list, name='products_list'),
    path('products/<int:id>/', views.product_description, name='product_description')
]
