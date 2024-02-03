from rest_framework import serializers
from .models import ddjango


class ddjangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ddjango
        fields = ['id', 'name', 'description']

