from django.urls import include, path
from rest_framework import routers
from .categories import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
router.register('itemimage', views.ItemImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
