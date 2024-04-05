from django.shortcuts import render

# Displays the content of the Home page
def home(request):
    return render(request, 'home/index.html')