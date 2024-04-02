from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'guests', 'first_name', 'last_name', 'phone', 'email', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'max': 8}),
            'message': forms.Textarea(attrs={'class': 'message-textarea', 'rows': 4}),
        }
