from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompilationViewSet

router = DefaultRouter()
router.register('api', CompilationViewSet)


urlpatterns = [
]

urlpatterns += router.urls
