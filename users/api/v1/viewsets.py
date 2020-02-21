from rest_framework import authentication
from users.models import OOO, User
from .serializers import OOOSerializer, UserSerializer
from rest_framework import viewsets


class OOOViewSet(viewsets.ModelViewSet):
    serializer_class = OOOSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = OOO.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = User.objects.all()
