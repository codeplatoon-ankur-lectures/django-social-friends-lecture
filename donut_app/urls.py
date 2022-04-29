from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("user-profiles", UserProfileViewSet, basename="user-profile")
router.register("friend-requests", FriendRequestViewSet, basename="friend-request")

urlpatterns = [
    path("", include(router.urls))
]