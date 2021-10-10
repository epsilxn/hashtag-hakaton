from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('parent', ParentViewSet)
router.register('children', ChildViewSet)

urlpatterns = router.urls
