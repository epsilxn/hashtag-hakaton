from rest_framework import routers
from django.urls import include
from .api import *

router = routers.DefaultRouter()
# router.register('auth/', include('djoser.urls'))
# router.register('auth/', include('djoser.urls.authtoken'))
router.register("me", UserViewSet)

urlpatterns = router.urls
