from django.urls import path
from.views import one,two,three

urlpatterns = [
    path('',one.as_view(),name='home'),
    path('api/',three.as_view(),name='base'),
    path('api/<int:pk>/',two.as_view(),name='base'),
    
]
