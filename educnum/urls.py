from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from courses.views import CourseListCreate, EnrollmentCreate
from payements.views import PaymentListCreate

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentification JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Courses & enrollment
    path('api/courses/', CourseListCreate.as_view(), name="course-list"),
    path('api/enroll/', EnrollmentCreate.as_view(), name="enroll"),

    # Payments
    path('api/payments/', PaymentListCreate.as_view(), name="payments"),
]
