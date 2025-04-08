from rest_framework.serializers import ModelSerializer

class ObjectSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'