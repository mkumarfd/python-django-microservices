from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
