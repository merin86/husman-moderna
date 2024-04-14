from django.contrib import admin
from .models import Dish

# Class to customize dishes in the admin interface


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')


admin.site.register(Dish, DishAdmin)
