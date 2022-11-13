from django.urls import path
from . import api

app_name='hotel'

urlpatterns = [
    path("cities/",api.city_list,name='All Cities'),#1
    path("cities/hotels/",api.HotelListView.as_view(),name='Filtered Hotels'),#2
    path("cities/hotels/<int:id>",api.hoteldetails,name='Hotel details'),#3
    path("cities/hotels/<int:id>/room",api.hotelrooms,name='Hotel room'),#3
    path("cities/hotels/room/<int:id>",api.roomdetails,name='Room Details'),#3
    path("cities/hotels/range",api.MODELItemViewSet.as_view({'get': 'list'}),name='range'),#2
]
