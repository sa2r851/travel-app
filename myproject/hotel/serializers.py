from rest_framework import serializers
from .models import *
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = ['hotel_name','hotel_star','hotel_images','fromwhere','ourdate']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields =fields = "__all__"

class RoomdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = "__all__"
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = ['room_name','room_image','price','room_bed']

class HoteldetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = "__all__"