from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from api.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name="Почта",
        unique=True
    )
    number = models.BigIntegerField(
        verbose_name="Номер телефона",
        blank=True,
        null=True
    )
    is_staff = models.BooleanField(
        verbose_name="Админ статус",
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name="Активность",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="Статус суперпользователя",
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        swappable = "AUTH_USER_MODEL"


class Item(models.Model):

    name = models.CharField(
        max_length=70,
        verbose_name="Название"
    )
    imageURL=models.ImageField(
        upload_to="static/",
        verbose_name="Изображене"
    )
    description=models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    price=models.PositiveIntegerField(
        verbose_name="Цена",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Cart(models.Model):

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        unique=False,
        verbose_name="Пользователь",
    )
    item=models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        unique=False,
        related_name="item",
        verbose_name="Товар",
    )
    count=models.SmallIntegerField(
        verbose_name="Количество"
    )

    class Meta:
        verbose_name="Корзина"
        verbose_name_plural="Корзины"


class Favorites(models.Model):

    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        unique=False,
        verbose_name="Пользователь",
    )
    item=models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        unique=False,
        verbose_name="Товар",
    )
    count=models.SmallIntegerField(
        verbose_name="Количество"
    )

    class Meta:
        verbose_name="Избранное"
        verbose_name_plural="Избранное"