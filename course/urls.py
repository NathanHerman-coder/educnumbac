from django.urls import path, include
from rest_framework import routers
from courses.views import CourseViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # browsable login
]
