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

class TownListView(generics.ListAPIView):
    queryset = town.objects.all()
    serializer_class = TownSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['city_in']


class HallListView(generics.ListAPIView):
    queryset = hall.objects.all()
    serializer_class = WeddingSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['hall_name','address']
    filterset_fields = ['number_people', 'the_city','the_town']
    ordering_fields = ["price"]



@api_view(['GET'])
def halldetails(request,id):
    details=hall.objects.get(id=id)
    data=HalldetailsSerializer(details).data
    return Response({'data':data})

class StatementItemFilter(filters.FilterSet):
    price_between=filters.NumericRangeFilter(field_name='price', label="Number (Between)")
    class Meta:
        model = hall
        fields = [
            "price_between"
        ]
class PricerangeViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = hall.objects.all()
    filterset_class = StatementItemFilter
    serializer_class = WeddingSerializer
