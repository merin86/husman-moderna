from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Reservation class model which stores information about table reservations at a restaurant
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,15}$', 'Only numbers are allowed.')])
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.first_name} {self.last_name} on {self.date}"