from django.urls import path, include
from api.views import ItemAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"api/items", ItemAPI)

urlpatterns = [
    path('', include(router.urls)),
]