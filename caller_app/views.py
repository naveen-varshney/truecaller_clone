from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view,permission_classes,action
from rest_framework import permissions, viewsets
from .serializers import *


class UserViewset(viewsets.ModelViewSet):
    """
    Viewsets for users
    """
    queryset            = User.objects.filter(is_staff=False)
    serializer_class    = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class UserProfileViewset(viewsets.ModelViewSet):
    """

    """
    queryset            = UserProfile.objects.all()
    serializer_class    = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )



class UserContactViewset(viewsets.ModelViewSet):
    """
    viewsets for usercontacts
    """
    queryset            = UserContact.objects.all()
    serializer_class    = UserContactSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @action(methods=['GET'],detail=False,permission_classes=[permissions.IsAuthenticated],url_path='search-by-name')
    def search_by_name(self, request, pk=None):
        queryset = self.queryset
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__iexact=name)

        return Response(queryset, status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False,permission_classes=[permissions.IsAuthenticated],url_path='search-by-number')
    def search_by_number(self, request, pk=None):
        queryset = self.queryset
        phone_number = self.request.query_params.get('phone_number', None)
        if phone_number:
            queryset = queryset.filter(phone_number__iexact=phone_number)

        return Response(queryset, status=status.HTTP_200_OK)
