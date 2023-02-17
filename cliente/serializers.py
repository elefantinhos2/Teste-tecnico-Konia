from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators = [UniqueValidator(queryset = User.objects.all(), message = "username already existy")]
    )


    class Meta: 
        model = User
        exclude = ["is_active", "is_staff", "groups", "user_permissions"]
        read_only_fields = ["id", "date_joined", "is_superuser", "last_login"]
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)

        return user


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ["is_staff", "groups", "user_permissions","email"]
        read_only_fields = ["id", "date_joined", "is_superuser", "is_active", "last_login"]
        extra_kwargs = {"password": {"write_only": True}}

