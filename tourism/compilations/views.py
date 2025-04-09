from rest_framework.viewsets import ModelViewSet
from .models import Compilation
from .serializers import CompilationSerializer

# Create your views here.

class CompilationViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Compilation.objects.all()
    serializer_class = CompilationSerializer

