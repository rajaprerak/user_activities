from .models import User, Activity
from rest_framework import serializers

"""
Serializers allow complex data such as query set and model instances to be converted to native python
which can then be rendered to json, xml or other content types
"""


class ActivitySerializer(serializers.ModelSerializer):
    """
    Activity Serializer:- Contains fields start time and end time
    """

    class Meta:
        model = Activity
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer:-   Contains nested serializer to show activity timings
                        Also contains its own fields such as name, id and time zone.
    """
    activity_periods = ActivitySerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
