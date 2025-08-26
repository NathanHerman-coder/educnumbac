from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("pending","Pending"),("completed","Completed")], default="completed")

    def __str__(self):
        return f"Payment {self.id} - {self.user.username}"
