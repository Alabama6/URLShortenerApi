from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = URL
        fields = ('original_url', 'short_url')
