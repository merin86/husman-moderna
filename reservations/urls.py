from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('book/', views.book_reservation, name='book_reservation'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('edit/<int:reservation_id>/', views.edit_reservation,
         name='edit_reservation'),
    path('<int:pk>/delete/', views.delete_reservation,
         name='delete_reservation'),
    path('large_reservation/', views.large_reservation,
         name='large_reservation'),
]
