from django.contrib import admin
from .models import Dish


class DishAdmin(admin.ModelAdmin):
    """
    Class to customize dishes in the admin interface
    """
    list_display = ('name', 'description', 'price', 'category')


admin.site.register(Dish, DishAdmin)
