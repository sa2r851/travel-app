from rest_framework import serializers
from .models import *
class HallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = hallimage
        fields = '__all__'
class WeddingSerializer(serializers.Serializer):
    class Meta:
        model = hall
        fields = ['hall_name','price','halls_images','address','location']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields =fields = "__all__"

class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = town
        fields =fields = "__all__"


class HalldetailsSerializer(serializers.ModelSerializer):
    images= HallImageSerializer(source='hallimage_set', many=True, read_only=True)
    class Meta:
        model = hall
        fields = ['id','uploaded_images','image','price','number_people','price_list','number_people','address','hall_name']
        extra_kwargs = {"user":{"read_only":True}}
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        hall = hall.objects.create(title=validated_data.get('title', 'no-title'),
                                   user_id=1)
        for image_data in images_data.values():
            hallimage.objects.create(hall=hall, image=image_data)
        return hall


