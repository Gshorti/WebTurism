from rest_framework.serializers import ModelSerializer

class AttractionSerializer(ModelSerializer):

    class Meta:

        fields = '__all__'
