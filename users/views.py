from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from .serializers import UserSerializer, UserLoginTokenSerializer
from .models import User
sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


# Login Locally
class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data

        if not data.get('password'):
            raise exceptions.ValidationError('Must include "email" and "password".')
        if not data.get('email'):
            raise exceptions.ValidationError('Must include "email" and "password".')

        # Authentication
        user = authenticate(email=data.get('email'), password=data.get('password'))

        if user:
            if not user.is_active:
                raise exceptions.ValidationError('User account is disabled.')

                # if not user.is_verified:
                #     raise exceptions.ValidationError('E-mail is not verified.')

        else:
            raise exceptions.ValidationError('Unable to log in with provided credentials.')

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'user': UserSerializer(user).data,
            'token': UserLoginTokenSerializer(token).data
        }, status=status.HTTP_200_OK)


# Retrieve / update user
class UserRetrieveAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        user_qs = User.objects.get(pk=user_id)
        user = UserSerializer(user_qs).data

        return Response(user, status=status.HTTP_200_OK)
