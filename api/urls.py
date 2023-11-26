from django.urls import path
from .views import *
urlpatterns = [
    path('users/', UserApiView.as_view()),
    path('', KitoblarApiView.as_view()),
    path('haridlar/', HaridlarApiView.as_view()),
]