from .models import User,Activity
from .serializers import UserSerializer
from rest_framework import viewsets

class UserActivitiesAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
