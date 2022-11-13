from rest_framework import generics
from rest_framework import filters
import django_filters
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from psycopg2.extras import DateRange
from rest_framework import viewsets


@api_view(['GET'])
def heggdetails(request,id):
    details=hegg.objects.get(id=id)
    data=HeggSerializer(details).data
    return Response({'data':data})

@api_view(['GET'])
def umrahdetails(request,id):
    details=umrah.objects.get(id=id)
    data=UmrahSerializer(details).data
    return Response({'data':data})
# umrah
class TripListView(generics.ListAPIView):
    queryset = umrah.objects.all()
    serializer_class =UmrahlistSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['company']
    filterset_fields = ["durtion"]
    ordering_fields = ["price","ourdata"]

# Range datefilter
class StatementItemFilter(filters.FilterSet):
    date_between = filters.DateFromToRangeFilter(field_name="ourdate", label="Date (Between)")
    price_between=filters.NumericRangeFilter(field_name="price", label="Number (Between)")
    class Meta:
        model = umrah
        fields = [
            "date_between",
            "price_between"
        ]
class MODELItemViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = umrah.objects.all()
    filterset_class = StatementItemFilter
    serializer_class = UmrahlistSerializer

# hegg
class HeggFilter(filters.FilterSet):
    price_between=filters.NumericRangeFilter(field_name="price", label="Number (Between)")
    class Meta:
        model = hegg
        fields = [
            "price_between"
        ]
class HeggViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = hegg.objects.all()
    filterset_class = StatementItemFilter
    serializer_class = UmrahlistSerializer

class HeggListView(generics.ListAPIView):
    queryset = umrah.objects.all()
    serializer_class =UmrahlistSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['company']
    filterset_fields = ["durtion"]
    ordering_fields = ["price","ourdata"]