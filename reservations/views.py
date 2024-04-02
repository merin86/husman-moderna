from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required

@login_required
def book_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('my_reservations')
    else:
        form = ReservationForm()
    return render(request, 'reservations/book_reservation.html', {'form': form})

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})