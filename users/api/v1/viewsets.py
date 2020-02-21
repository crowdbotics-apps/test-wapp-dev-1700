from rest_framework import authentication
from users.models import OOO
from .serializers import OOOSerializer
from rest_framework import viewsets


class OOOViewSet(viewsets.ModelViewSet):
    serializer_class = OOOSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = OOO.objects.all()
