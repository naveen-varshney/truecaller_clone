from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'contacts', UserContactViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
