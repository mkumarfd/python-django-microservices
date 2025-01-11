from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders import views

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename='orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
