from django.shortcuts import render
from .models import AboutPage


# Displays the content of the About page
def about(request):
    about_page = AboutPage.objects.first()
    context = {
        'about_page': about_page
    }
    return render(request, 'about/about.html', context)
