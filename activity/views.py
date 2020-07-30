from .models import User, Activity
from .serializers import UserSerializer
from rest_framework import viewsets


class UserActivitiesAPI(viewsets.ModelViewSet):
    """
    View is callable which takes request and return response
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
