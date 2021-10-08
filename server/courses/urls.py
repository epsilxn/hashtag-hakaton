from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('teacher', TeacherViewSet)
router.register('course', CoursesViewSet)

urlpatterns = router.urls
