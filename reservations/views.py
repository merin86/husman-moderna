from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def book_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']

            existing_reservation = Reservation.objects.filter(user=request.user, date=date).exists()

            if existing_reservation:
                messages.error(request, "You already have a reservation on this date.")
                return render(request, 'reservations/book_reservation.html', {'form': form})

            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.time = form.cleaned_data.get('time')
            reservation.save()
            messages.success(request, "Your reservation has been successfully booked.")
            return redirect('reservations:my_reservations')
    else:
        form = ReservationForm()
    return render(request, 'reservations/book_reservation.html', {'form': form})


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})


@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            date = form.cleaned_data['date']

            existing_reservation = Reservation.objects.filter(
                user=request.user, 
                date=date
            ).exclude(id=reservation_id).exists()

            if existing_reservation:
                messages.error(request, "You already have a reservation on this date.")
                return render(request, 'reservations/book_reservation.html', {'form': form, 'is_editing': True})

            form.save()
            messages.success(request, "Your reservation has been successfully updated.")
            return redirect('reservations:my_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/book_reservation.html', {'form': form, 'is_editing': True})


@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "The reservation has been successfully deleted.")
        return redirect('reservations:my_reservations')
    else:
        return redirect('reservations:my_reservations')
