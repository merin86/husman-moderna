from django.shortcuts import render
from .models import AboutPage


def about(request):
    """
    Displays the content on the About page
    """
    about_page = AboutPage.objects.first()
    context = {
        'about_page': about_page
    }
    return render(request, 'about/about.html', context)
