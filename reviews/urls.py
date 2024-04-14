from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('create/', views.review_create, name='review_create'),
    path('<int:review_id>/update/', views.review_update, name='review_update'),
    path('<int:review_id>/delete/', views.review_delete, name='review_delete'),
]
