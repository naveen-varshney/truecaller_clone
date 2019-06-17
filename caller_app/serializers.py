from rest_framework import fields, serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class UserContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserContact
        fields = ('name','phone_number','email')


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email', read_only=True)
    user = serializers.ReadOnlyField(source='user.id', read_only=True)

    class Meta:
        model = User
        fields = ('user','name','email','phone_number')
