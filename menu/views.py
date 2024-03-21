from django.shortcuts import render
from .models import Dish

# Create your views here.

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})


