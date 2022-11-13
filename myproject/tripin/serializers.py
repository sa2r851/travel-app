from rest_framework import serializers
from .models import *
class TripinSerializer(serializers.ModelSerializer):
    class Meta:
        model = trip
        fields = ['company','price','trip_images','destination','durtion']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields =fields = "__all__"


class TripdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = trip
        fields = "__all__"

