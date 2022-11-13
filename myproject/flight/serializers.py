from rest_framework import serializers
from .models import *
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = travel
        fields = ['company','price','destination','fromwhere','ourdate']



class TripdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = travel
        fields = "__all__"
