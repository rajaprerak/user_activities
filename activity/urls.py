from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register("UserActivity",views.Userapi)
router.register("RegisterActivity",views.Activitiesapi)

urlpatterns = [
    path('', include(router.urls)),
]
