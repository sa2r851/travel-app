from rest_framework import serializers
from .models import *
class TripoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = travel
        fields = ['company','price','trip_images','destination','durtion']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields =fields = "__all__"


class TripdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = travel
        fields = "__all__"

