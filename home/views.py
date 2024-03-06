from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .serializer import *
from django.contrib.auth.models import User


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetriveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer