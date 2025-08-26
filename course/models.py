from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='courses/pdfs/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
