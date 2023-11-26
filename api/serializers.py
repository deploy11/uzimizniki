from .models import *
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class KitoplarSerializer(ModelSerializer):
    class Meta:
        model = Kitoblar
        fields = ('__all__')

class HaridlarSerializer(ModelSerializer):
    class Meta:
        model = Haridlar
        fields = ('__all__')