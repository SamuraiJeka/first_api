from rest_framework import serializers
from .models import User, Item, Cart

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
