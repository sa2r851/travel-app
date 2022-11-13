from rest_framework import serializers
from .models import *



class ApartlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = apart
        fields = ['type_apart','apart_images','price_night','price_month','the_city','the_town','address','bathroom','title','rooms','id']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields =fields = "__all__"
class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = town
        fields =fields = "__all__"



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"

class ApartdetailsSerializer(serializers.ModelSerializer):
    apartment_image = ImageSerializer(many=True,required=False)

    class Meta:
        model = apart
        fields ="__all__"