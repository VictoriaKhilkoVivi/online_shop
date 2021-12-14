from django.urls import include, path
from rest_framework import routers
from shop.categories import views


router = routers.DefaultRouter()
router.register('categories', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
