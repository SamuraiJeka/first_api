from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, mixins, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item, User, Cart
from .seriailzers import ItemSerializer, UserSerializer, CartSerializer
from .permissioms import IsAdminOrReadOnly

mixins = [viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin]

class ItemViewset(*mixins):
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


class CartViewset(viewsets.ModelViewSet):
    
    queryset = Cart.objects.all()

    def get_serializer(self, *args, **kwargs):
        return CartSerializer(*args, **kwargs)

    def get_queryset(self):
        email = self.request.query_params.get('email')
        return Cart.objects.filter(user__email=email)
    
    @action(detail=False, methods=['post'], url_path='create-cart-post')
    def create_book_post(self, request):
        serializer = CartSerializer(data=(request.data | {"user": request.data['user']}))

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
