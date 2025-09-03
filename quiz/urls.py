from rest_framework.routers import DefaultRouter
from .api import QuizViewSet, AttemptViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'attempts', AttemptViewSet, basename='attempt')

urlpatterns = router.urls

