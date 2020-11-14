from rest_framework import serializers #need for rest 
from .models import cool

class sos(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = cool
