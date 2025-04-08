from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AttractionViewSet

router = DefaultRouter()
router.register('attractions', AttractionViewSet)


urlpatterns = [
    path('api/', admin.site.urls),
]

urlpatterns += router.urls
