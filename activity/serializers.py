from .models import User,Activity
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('start_time','end_time')
    
class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = '__all__'
        
