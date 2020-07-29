from .models import User,Activity
from .serializers import UserSerializer,ActivitySerializer
from rest_framework import viewsets

class Userapi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Activitiesapi(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer