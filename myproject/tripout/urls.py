from django.urls import path
from . import api

app_name='tripout'

urlpatterns = [
    path("countries/",api.country_list,name='All Cities'),
    path("countries/trips/",api.TripListView.as_view(),name='Filtered trips'),
    path("countries/trips/<int:id>",api.tripoutdetails,name='tripin details'),
    path("countries/trips/range",api.MODELItemViewSet.as_view({'get': 'list'}),name='range'),

]