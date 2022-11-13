from django.urls import path
from . import api

app_name='honey_moon'

urlpatterns = [
    path("moons/",api.MoonListView.as_view(),name='Filtered Honey Moon'),#1
    path("moons/<int:id>",api.moondetails,name='Honey Moon details'),#2
    path("moons/range",api.MODELItemViewSet.as_view({'get': 'list'}),name='range'),#1
]
