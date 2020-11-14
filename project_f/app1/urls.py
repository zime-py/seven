from django.urls import path
from.views import one,two,three,four

urlpatterns = [
    path('',one.as_view(),name='home'), #for show model data in html page
    path('api/',two.as_view(),name='base'),  #for show model data in rest format
    path('api/new/',three.as_view(),name='base'), #for create/add new data
    path('api/<int:pk>/',four.as_view(),name='base'), #for red,update,delete data
]
