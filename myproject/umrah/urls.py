from django.urls import path
from . import api

app_name='umrah'

urlpatterns = [
    path("hegg/trips/",api.HeggListView.as_view(),name='Filtered hegg'),
    path("hegg/trips/<int:id>",api.heggdetails,name='tripin details'),
    path("hegg/",api.MODELItemViewSet.as_view({'get': 'list'}),name='range hegg'),
    path("umrah/",api.MODELItemViewSet.as_view({'get': 'list'}),name='range umrah'),
    path("umrah/trips/",api.TripListView.as_view(),name='Filtered umrah'),
    path("umrah/trips/<int:id>",api.umrahdetails,name='umrah details'),
]