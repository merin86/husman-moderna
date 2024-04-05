from django.shortcuts import render
from .models import Dish


# The menu view-function gathers and organizes dishes for menu page
def menu(request):
    appetizers = Dish.objects.filter(category='Appetizer')
    main_courses = Dish.objects.filter(category='Main Course')
    desserts = Dish.objects.filter(category='Dessert')
    
    context = {
        'appetizers': appetizers,
        'main_courses': main_courses,
        'desserts': desserts,
    }
    return render(request, 'menu/menu.html', context)
