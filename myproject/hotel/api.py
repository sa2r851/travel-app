from rest_framework import generics
from rest_framework import filters
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets

@api_view(['GET'])
def city_list(request):
    all_address=city.objects.all()
    data=CitySerializer(all_address,many=True).data
    return Response ({'data':data})

@api_view(['GET'])
def roomdetails(request,id):
    details=room.objects.get(id=id)
    data=RoomdetailsSerializer(details).data
    return Response({'data':data})
@api_view(['GET'])
def hoteldetails(request,id):
    details=hotel.objects.get(id=id)
    data=HoteldetailsSerializer(details).data
    return Response({'data':data})
    
@api_view(['GET'])
def hotelrooms(request,id):
    details=room.objects.get(id=hotel.pk)
    data=RoomsSerializer(details).data
    return Response({'data':data})

class HotelListView(generics.ListAPIView):
    queryset = hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['hotel_name','address']
    filterset_fields = ['location', 'hotel_star','include_meals','allowed_pets','free_cancellation','pay_arrival']
    ordering_fields = ["lowest_price","hotel_star"]
class StatementItemFilter(filters.FilterSet):
    price_between=filters.RangeFilter(field_name="lowest_price", label="Number (Between)")
    class Meta:
        model = hotel
        fields = [
            "price_between"
        ]

class MODELItemViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = hotel.objects.all()
    filterset_class = StatementItemFilter
    serializer_class = HotelSerializer
