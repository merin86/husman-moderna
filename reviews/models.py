from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    """
    The Review model to store user reviews. This model links to
    the :model:`auth.User` to associate reviews with specific
    users and their actions within the system.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(max_length=5000, null=False, blank=False)
    rating = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | written by {self.user}"

    class Meta:
        ordering = ["-created_at"]
