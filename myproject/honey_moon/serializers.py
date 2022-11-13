from rest_framework import serializers
from .models import *
class HoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = moon
        fields = ['company','price','trip_images','destination','durtion']




class MoondetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = moon
        fields = "__all__"

