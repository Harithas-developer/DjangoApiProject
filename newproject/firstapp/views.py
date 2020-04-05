from rest_framework import viewsets

from .serializers import ActivitySerializer ,NameSerializer
from .models import Name,AcitvityPeriod


class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = AcitvityPeriod.objects.all()
    serializer_class = ActivitySerializer