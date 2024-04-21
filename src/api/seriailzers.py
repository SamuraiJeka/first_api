from djoser.serializers import UserCreateSerializer

from rest_framework import serializers
from .models import User, Item, Cart, Favorites


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Item
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'imageURL', 'price']
        


class UserCastomCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'number']
        exclude_fields = ['password',]


class CartSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    count = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ['item', 'count',]


class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    description = serializers.SlugRelatedField(slug_field='description', read_only=True)

    class Meta:
        model = Cart
        fields = ['item', 'description']


class AddFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'