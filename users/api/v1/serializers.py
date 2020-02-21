from rest_framework import serializers
from users.models import OOO, User


class OOOSerializer(serializers.ModelSerializer):
    class Meta:
        model = OOO
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
