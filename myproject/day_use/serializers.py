from rest_framework import serializers
from .models import *
class DayuseSerializer(serializers.ModelSerializer):
    class Meta:
        model = daytrip
        fields = ['company','price','trip_images','destination','fromwhere']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields =fields = "__all__"


class TripdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = daytrip
        fields = "__all__"

