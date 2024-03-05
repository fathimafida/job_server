from rest_framework import serializers
from ..models import PostJob

# from django.contrib.auth.models import User as CustomUser


class PostJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJob
        fields = "__all__"


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ("email", "password", "name")
#         extra_kwargs = {"password": {"write_only": True}}

# def create(self, validated_data):
#     user = CustomUser.objects.create(**validated_data)
#     return user
