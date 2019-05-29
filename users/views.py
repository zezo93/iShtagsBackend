from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import UserSerializer
from .models import User


# Create your views here.
class UserRetrieveAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        user_qs = User.objects.get(pk=user_id)
        user = UserSerializer(user_qs).data

        return Response(user, status=status.HTTP_200_OK)
