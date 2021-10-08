from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('teacher', TeacherViewSet)
router.register('course', CoursesViewSet)
router.register('lesson', LessonsViewSet)
router.register('schedule', LessonsViewSet)

urlpatterns = router.urls
