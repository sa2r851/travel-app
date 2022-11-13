from rest_framework import serializers
from .models import *
class HegglistSerializer(serializers.ModelSerializer):
    class Meta:
        model = umrah
        fields = ['company','price','durtion']

class UmrahSerializer(serializers.ModelSerializer):
    class Meta:
        model = umrah
        fields =fields = "__all__"


class HeggSerializer(serializers.ModelSerializer):
    class Meta:
        model = hegg
        fields = "__all__"

class UmrahlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = umrah
        fields = ['company','price','durtion']