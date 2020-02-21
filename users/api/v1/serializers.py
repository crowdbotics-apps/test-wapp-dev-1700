from rest_framework import serializers
from users.models import OOO


class OOOSerializer(serializers.ModelSerializer):
    class Meta:
        model = OOO
        fields = "__all__"
