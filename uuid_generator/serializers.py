from rest_framework import serializers
from .models import UUID_table


class UuidSerializer(serializers.ModelSerializer):
    class Meta:
        model = UUID_table
        fields = ["id", "key", "value"]
