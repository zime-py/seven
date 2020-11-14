from django.shortcuts import render
from django.views.generic import ListView #use for listview purpose
from.models import cool     #include models.py
from rest_framework import generics #for rest
from .serializers import sos #include serializes.py

class one(ListView):
    template_name='home.html'
    model=cool

#for api view
class two(generics.ListAPIView): #'ListAPIView'  all data in list array
    queryset = cool.objects.all()
    serializer_class = sos
    template_name='base.html' 

class three(generics.ListCreateAPIView): # 'ListCreateAPIView' create/add new date 
    queryset = cool.objects.all().order_by('id')  #show all list data in accensing, (1.2.3.4.....)
    #queryset = cool.objects.all().order_by('-id') #show all data in deaccensing, (.......4.3.2.1)
    #queryset = cool.objects.all().order_by('-id')[:1] #show only last added data
    serializer_class = sos
    template_name='base.html'

#for detail view
class four(generics.RetrieveUpdateDestroyAPIView): #genarelly write 'RetrieveAPIView' but here RetrieveUpdateDestroyAPIView
    queryset = cool.objects.all()                 #cause of red, update and delete post purpose
    serializer_class = sos
    template_name='base.html'

