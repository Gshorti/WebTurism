from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ObjectViewSet

router = DefaultRouter()
router.register('api', ObjectViewSet)


urlpatterns = [
]

urlpatterns += router.urls
