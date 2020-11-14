from rest_framework import serializers
from app1.models import cool
class sos(serializers.ModelSerializer):
    class Meta:
        model = cool
        fields = '__all__'


