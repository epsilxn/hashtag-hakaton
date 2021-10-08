from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('parent', ParentViewSet)

urlpatterns = router.urls
