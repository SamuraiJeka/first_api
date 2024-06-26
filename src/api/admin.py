from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model=User
    list_display=[
        "email",
        "is_staff",
    ]
    list_filter=[
        "is_staff"
    ]
    fields=[
        "email",
        "number",
        "password"
    ]
    readonly_fields=[
        "email",
        "password"
    ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model=Item
    list_display=[
        "name",
        "id",
        "price",
        "imageURL"
    ]
    fields=[
        "name",
        "description",
        "price",
        "imageURL",
    ]
    readonly_fields=["get_image"]

    def get_image(self, item: Item):
        if item.imageURL:
            return mark_safe(f"<img src='{item.imageURL.url}' width=50 length=60>")
        else:
            return "Без изображения"
        
    get_image.short_description="Изображение"


@admin.register(Cart)
class CatrAdmin(admin.ModelAdmin):
    model=Cart
    list_display=[
        "user",
        "item",
        "count",
    ]

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    model=Favorites
    list_display=[
        "user",
        "item",
    ]