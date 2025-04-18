from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import ObjectSerializer
from .models import Objects
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TagFilter

# Create your views here.

class ObjectViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Objects.objects.all()
    serializer_class = ObjectSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'description', 'address', 'price']
    ordering_fields = ['id']


    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        res = TagFilter(request, response)
        return Response(res)