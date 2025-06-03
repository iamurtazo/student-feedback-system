from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    # Feedback model fields
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 rating
    comment = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('addressed', 'Addressed')],
        default='pending'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course} ({self.rating}/5)"

# Note: We'll use Django's built-in User model for admin authentication
# instead of creating a separate Admin model for better security and features
