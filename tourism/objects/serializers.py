from rest_framework.serializers import ModelSerializer
from .models import Objects

class ObjectSerializer(ModelSerializer):

    class Meta:
        model = Objects
        fields = '__all__'