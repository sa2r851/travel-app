from django.urls import path
from . import api

app_name='day_use'

urlpatterns = [
    #customer
    path("trips/",api.TripListView.as_view(),name='Filtered trips'),# 1
    path("trips/range",api.MODELItemViewSet.as_view({'get': 'list'}),name='range'),# 1
    path("trips/<int:id>",api.tripdetails,name='Day-use details'),# 2






]
