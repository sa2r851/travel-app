from django.urls import path
from . import api
app_name='apartment'

urlpatterns = [
     path("cities/",api.city_list,name='All Cities'),#1
     path("cities/towns/",api.TownListView.as_view(),name='Filtered Town'),#2
     path("images/",api.Files_APIView.as_view(),name='images'),#2
     path("cities/towns/apart",api.ApartListView.as_view(),name='Filtered Apart'),#3
     path("cities/towns/range",api.MODELItemViewSet.as_view({'get': 'list'}),name='range'),#3
     path("cities/towns/apart/<int:id>",api.apartdetails,name='Apartment Details'),#4
     

]
