from django.shortcuts import render


def home(request):
    """
    Displays the content of the Home page
    """
    return render(request, 'home/index.html')
