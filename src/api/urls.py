from django.urls import path, include, re_path
from api.views import ItemViewset, UserViewset, CartViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"api/items", ItemViewset)
# router.register(r"api/users", UserViewset, basename='User')
router.register(r"api/cart", CartViewset)

urlpatterns = [
    path('', include(router.urls)),
    path(r"api/user", UserViewset.as_view())
]