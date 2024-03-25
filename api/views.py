from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from .models import Item, User
from .seriailzers import ItemSerializer, UserSerializer


class ItemViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer