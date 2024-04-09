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
    
    user = serializers.SlugRelatedField(slug_field="email", queryset=User.objects.all(), write_only=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), write_only=True)
    item = ItemSerializer(read_only=True)


    # def to_representation(self, instance):
    #     return super().to_representation(instance)

    # @property
    # def data(self):
    #     data = super().data
    #     if (title := data["item"]) is not None:
    #         data["item"] = Item.objects.get(id=title).name
    #     return data
    
    # description = serializers.SerializerMethodField()
    # def get_description(self, instance):
    #     return instance.item.description
    
    class Meta:
        model = Cart
        fields = ['item', 'count', 'item_id', 'user']

