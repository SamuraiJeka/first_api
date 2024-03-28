from django.shortcuts import render
from rest_framework import viewsets, generics, mixins

from .models import Item, User, Cart
from .seriailzers import ItemSerializer, UserSerializer, CartSerializer
from .permissioms import IsAdminOrReadOnly

mixins = [viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin]

class ItemViewset(*mixins):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAdminOrReadOnly, )


class UserViewset(*mixins):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CartViewset(*mixins):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        return Cart.objects.filter(user__email=email)
    
    permission_classes = (IsAdminOrReadOnly, )