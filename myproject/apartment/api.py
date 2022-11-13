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
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

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

class ApartListView(generics.ListAPIView):
    queryset = apart.objects.all()
    serializer_class = ApartlistSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['address']
    filterset_fields = ['the_city', 'the_town','type_apart','rooms','furniture','bed']
    ordering_fields = ["price_night"]

class StatementItemFilter(filters.FilterSet):
    pricen_between=filters.RangeFilter(field_name="price_night", label="Night (Between)")
    pricem_between=filters.RangeFilter(field_name="price_month", label="Month (Between)")

    class Meta:
        model = apart
        fields = [
            "pricen_between",
            "pricen_between"

        ]

class MODELItemViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = apart.objects.all()
    filterset_class = StatementItemFilter
    serializer_class = ApartlistSerializer

@api_view(['GET'])
def apartdetails(request,id):
    details=apart.objects.get(id=id)
    data=ApartdetailsSerializer(details).data
    return Response({'data':data})


class Files_APIView(APIView):
    #parser_class = (FileUploadParser, )
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    #permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):

        serializer = ImageSerializer(data=request.data)
        
        files_list = request.FILES.getlist('one_file')
        if serializer.is_valid():
            for item in files_list:
                f = Images.objects.create(apart=request.data['apart'], one_file=item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)