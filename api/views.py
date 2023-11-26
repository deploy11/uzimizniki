from django.shortcuts import render
from rest_framework.generics import *
from django.views.generic import *
from .serializers import *
from .models import User
# Create your views here.
class UserApiView(ListCreateAPIView,UpdateAPIView):
    queryset = User.objects.all()
    serializer_class  = UserSerializer

class KitoblarApiView(ListCreateAPIView,UpdateAPIView):
    queryset = Kitoblar.objects.all()
    serializer_class  = KitoplarSerializer

class HaridlarApiView(ListCreateAPIView,UpdateAPIView):
    queryset = Haridlar.objects.all()
    serializer_class  = HaridlarSerializer