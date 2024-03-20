from rest_framework import serializers
from .models import user_details  

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_details 
        fields = '__all__'
