from django.urls import path,include
from api.views import TodoViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'todos',TodoViewset)


urlpatterns = [
    path('', include(router.urls)),
]