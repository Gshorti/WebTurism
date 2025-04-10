from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import AttractionSerializer
from .models import Attraction
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TagFilter
# Create your views here.

class AttractionViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'description', 'address', 'price']
    ordering_fields = ['id']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        res = TagFilter(request, response)
        return Response(res)