from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ObjectViewSet

router = DefaultRouter()
router.register('attractions', ObjectViewSet)


urlpatterns = [
    path('api/', admin.site.urls),
]

urlpatterns += router.urls
