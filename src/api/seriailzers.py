from rest_framework import serializers
from .models import User, Item, Cart


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Item
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'imageURL', 'price']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'id']


class CartSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    count = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ['item', 'count',]


class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['item', 'count', 'user']

