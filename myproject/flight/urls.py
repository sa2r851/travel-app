from django.urls import path
from . import api

app_name='flight'

urlpatterns = [
    path("trips/",api.TripListView.as_view(),name='Filtered trips'),
    path("trips/<int:id>",api.flightdetails,name='flight details'),# 2
    path("trips/range",api.MODELItemViewSet.as_view({'get': 'list'}),name='range'),# 1

]