from django.contrib.auth import authenticate
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView, Request, Response, status

from utils.mixins import SerializerByMethodMixin

from .models import User
from .serializers import UserListSerializer, UserSerializer


class UserView(SerializerByMethodMixin, ListCreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_map = {
        "GET": UserListSerializer,
        "POST": UserSerializer
    }


