from django.shortcuts import render
from django.views.generic import ListView #use for listview purpose
from.models import cool     #include models.py
from rest_framework import generics#, permissions #for rest view lavel permission 
from .serializers import sos #include serializes.py
from .permissions import IsAuthorOrReadOnly # new

class one(ListView):
    template_name='home.html'
    model=cool

#for api view
class two(generics.ListAPIView): #'ListAPIView'  all data in list array
    #permission_classes = (permissions.IsAuthenticated,) #a khane dile admin logout takle all data show korbe na but end point show korbe
    queryset = cool.objects.all()                       #not work(8000/api) but work (8000/api/1)
    serializer_class = sos
    template_name='base.html' 

class three(generics.ListCreateAPIView): # 'ListCreateAPIView' create/add new date
    #permission_classes = (permissions.IsAuthenticated,)  #ekhane dile post/ crate option takbe na, but all post deka and update,delete kora jabe
    queryset = cool.objects.all().order_by('id')  #show all list data in accensing, (1.2.3.4.....)
    serializer_class = sos
    template_name='base.html'

#for detail view
class four(generics.RetrieveUpdateDestroyAPIView): #genarelly write 'RetrieveAPIView' but here RetrieveUpdateDestroyAPIView
    #permission_classes = (permissions.IsAuthenticated,) # not show post,put,delete option 
    queryset = cool.objects.all()                            #cause of red, update and delete post purpose
    serializer_class = sos
    template_name='base.html'
    permission_classes = (IsAuthorOrReadOnly,) # new
