from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pdf = models.FileField(upload_to="courses/pdfs/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.username} -> {self.course.name}"
