from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, mixins, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item, User, Cart
from .seriailzers import ItemSerializer, UserSerializer, CartSerializer, AddCartSerializer
from .permissioms import IsAdminOrReadOnly


class ItemViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAdminOrReadOnly, )


class UserViewset(APIView):
    
    def post(self, request, format=None):
        serialazer = UserSerializer(data=request.data)
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    queryset = Cart.objects.all()

    def get_serializer(self, *args, **kwargs):
        return CartSerializer(*args, **kwargs)

    def get_queryset(self):
        email = self.request.query_params.get('email')
        return Cart.objects.filter(user__email=email)
     

    def create(self, request):
        pk = User.objects.get(email=self.request.query_params.get('email')).pk
        print(self.request.query_params.get('email'))

        serializer = AddCartSerializer(data=(request.data | {"user": pk}))
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
