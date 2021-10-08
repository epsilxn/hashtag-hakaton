from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
# router.register('auth/', include('djoser.urls'))
# router.register('auth/', include('djoser.urls.authtoken'))


urlpatterns = router.urls