from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView

from .models import Item, User, Cart, Favorites
from .seriailzers import ItemSerializer, UserSerializer, CartSerializer, AddCartSerializer, FavoritesSerializer, AddFavoritesSerializer
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


class CartViewset(viewsets.GenericViewSet, mixins.ListModelMixin):    
    queryset = Cart.objects.all()

    def get_serializer(self, *args, **kwargs):
        return CartSerializer(*args, **kwargs)

    def get_queryset(self):
        email = self.request.query_params.get('email')
        return Cart.objects.filter(user__email=email)
     

    def create(self, request):
        email = User.objects.get(email=self.request.query_params.get('email'))
        serializer = AddCartSerializer(data=(request.data | {"user": email.pk}))
        
        if serializer.is_valid():

            item = Item.objects.get(pk=request.data.get('item'))

            try: 
                Cart.objects.get(user=email, item=item) in Cart.objects.filter(user=email.pk)
                cart = Cart.objects.get(user=email, item=item)
                cart.count += request.data.get('count')
                cart.save()
                return Response(status=status.HTTP_200_OK)
            except: 
                pass

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
"""
{
    "count": int,
    "item": int
}
"""


class FavoritesViewset(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        return Favorites.objects.filter(user__email=email)

    def create(self, request):
        email = User.objects.get(email=self.request.query_params.get('email'))
        serializer = AddFavoritesSerializer(data=(request.data | {"user": email.pk}))
        
        if serializer.is_valid():
            item = Item.objects.get(pk=request.data.get('item'))

            try: 
                if Favorites.objects.get(user=email, item=item) in Favorites.objects.filter(user=email.pk):
                    favorite = Favorites.objects.get(user=email, item=item)
                    favorite.delete()
                return Response(status=status.HTTP_200_OK)
            except: 
                pass

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)