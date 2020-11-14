from django.views.generic import DetailView,ListView
from rest_framework import generics
from .models import cool
from.serializers import sos



class one(ListView):
    template_name='home.html'
    model=cool

class three(generics.ListCreateAPIView):
    template_name='base.html'
    queryset = cool.objects.all()
    serializer_class = sos

class two(generics.RetrieveUpdateDestroyAPIView):
    queryset = cool.objects.all()
    serializer_class = sos
    template_name='base.html'






    

# Create your views here.
