from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('book/', views.book_reservation, name='book_reservation'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
]
