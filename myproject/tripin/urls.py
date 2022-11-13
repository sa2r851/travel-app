from django.urls import path
from . import api

app_name='tripin'

urlpatterns = [
    path("cities/",api.city_list,name='All Cities'),
    path("cities/trips/",api.TripListView.as_view(),name='Filtered trips'),
    path("cities/trips/<int:id>",api.tripindetails,name='tripin details'),
    path("cities/trips/range",api.MODELItemViewSet.as_view({'get': 'list'}),name='range'),
]