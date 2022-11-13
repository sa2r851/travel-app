from django.urls import path , include
from . import api
from rest_framework.routers import DefaultRouter
from . import views

app_name='wedding_halls'



urlpatterns = [
    path("cities/",api.city_list,name='All Cities'),#1
    path("cities/halls/",api.HallListView.as_view(),name='Filtered hall'),#2
    path("cities/halls/<int:id>",api.halldetails,name='Hall details'),#3
    path("cities/halls/price",api.PricerangeViewSet.as_view({'get': 'list'}),name='range price'),# 2


]
