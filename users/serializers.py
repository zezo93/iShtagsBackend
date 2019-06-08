from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginTokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
