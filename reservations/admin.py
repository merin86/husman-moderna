from django.contrib import admin
from .models import Reservation


# Class to handle bookings in the admin interface
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'guests', 'first_name', 'last_name', 'phone', 'email', 'user']
    list_filter = ['date', 'time', 'user']
    search_fields = ['first_name', 'last_name', 'email', 'phone']

admin.site.register(Reservation, ReservationAdmin)