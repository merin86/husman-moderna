from django import forms
from .models import Reservation

# This form class is used to create and edit reservations through the web interface
class ReservationForm(forms.ModelForm):
    TIME_CHOICES = [(f'{hour}:00', f'{hour}:00') for hour in range(11, 23)]

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.ChoiceField(choices=TIME_CHOICES)

# The Meta class specifies that this form is associated with the Reservation model and lists the fields to include in the form.
    class Meta:
        model = Reservation
        fields = ['date', 'guests', 'first_name', 'last_name', 'phone', 'email', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'max': 8}),
            'message': forms.Textarea(attrs={'class': 'message-textarea', 'rows': 4}),
        }
