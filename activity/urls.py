from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register("UserActivity",views.UserActivitiesAPI)

urlpatterns = [
    path('', include(router.urls)),
]
