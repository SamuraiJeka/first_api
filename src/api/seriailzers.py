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
        fields = ['email', 'password']


class CartSerializer(serializers.ModelSerializer):
    
    user = serializers.SlugRelatedField(slug_field="email", read_only=True)
    item = serializers.SlugRelatedField(slug_field="name", read_only=True)
    
    class Meta:
        model = Cart
        fields = ['item', 'count', 'user']
