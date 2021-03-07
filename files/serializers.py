from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserFiles

class UserAPI(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class FileAPI(serializers.ModelSerializer):
    class Meta:
        model = UserFiles
        fields = "__all__"

