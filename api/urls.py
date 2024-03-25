from django.urls import path, include
from api.views import ItemViewset, UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"api/items", ItemViewset)
router.register(r"api/users", UserViewset)

urlpatterns = [
    path('', include(router.urls)),
]