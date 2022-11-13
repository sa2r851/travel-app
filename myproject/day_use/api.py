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
def tripdetails(request,id):
    details=daytrip.objects.get(id=id)
    data=TripdetailsSerializer(details).data
    return Response({'data':data})


class TripListView(generics.ListAPIView):
    queryset = daytrip.objects.all()
    serializer_class = DayuseSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['company','address']
    filterset_fields = ['destination', 'fromwhere',]
    ordering_fields = ["price","ourdata"]

# Range datefilter
class StatementItemFilter(filters.FilterSet):
    date_between = filters.DateFromToRangeFilter(field_name="ourdate", label="Date (Between)")
    price_between=filters.NumericRangeFilter(field_name="price", label="Number (Between)")
    class Meta:
        model = daytrip
        fields = [
            "date_between",
            "price_between"
        ]
class MODELItemViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = daytrip.objects.all()
    filterset_class = StatementItemFilter
    serializer_class = DayuseSerializer




