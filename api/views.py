from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from .models import Item
from .seriailzers import ItemSerializer


class ItemAPI(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ['get']
