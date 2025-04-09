from rest_framework.serializers import ModelSerializer
from .models import Compilation

class CompilationSerializer(ModelSerializer):

    class Meta:
        model = Compilation
        fields = "__all__"