from rest_framework import filters
from .models import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets

class TripListView(generics.ListAPIView):
    queryset = travel.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['company']
    filterset_fields = ['destination', 'fromwhere',]
    ordering_fields = ["price","ourdata",'lunchtime']

# Range datefilter
class StatementItemFilter(filters.FilterSet):
    date_between = filters.DateFromToRangeFilter(field_name="ourdate", label="Date (Between)")
    price_between=filters.RangeFilter(field_name="price", label="Number (Between)")
    class Meta:
        model = travel
        fields = [
            "date_between",
            "price_between"
        ]
class MODELItemViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = travel.objects.all()
    filterset_class = StatementItemFilter
    serializer_class = FlightSerializer

@api_view(['GET'])
def flightdetails(request,id):
    details=travel.objects.get(id=id)
    data=TripdetailsSerializer(details).data
    return Response({'data':data})