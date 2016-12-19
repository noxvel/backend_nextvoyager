from django.shortcuts import render
from api.models import Item
from rest_framework import viewsets
from api.serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
