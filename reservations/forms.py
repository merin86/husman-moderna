from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation
from datetime import date


# This form class is used to create and edit reservations through the web
# interface
class ReservationForm(forms.ModelForm):
    TIME_CHOICES = [(f'{hour}:00', f'{hour}:00') for hour in range(11, 23)]

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.ChoiceField(choices=TIME_CHOICES)

# The Meta class specifies that this form is associated with the Reservation
# model and lists the fields to include in the form.
    class Meta:
        model = Reservation
        fields = ['date', 'guests', 'first_name', 'last_name', 'phone',
                  'email', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'max': 8}),
            'message': forms.Textarea(attrs={'class': 'message-textarea',
                                             'rows': 4}),
        }

    # Clears and validates the input for the 'first_name' field to ensure
    # it is not empty or just spaces.
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name').strip()
        if not first_name:
            raise forms.ValidationError("This field cannot be blank.")
        return first_name

    # Clears and validates the input for the 'last_name' field.
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name').strip()
        if not last_name:
            raise forms.ValidationError("This field cannot be blank.")
        return last_name

    # Clears and validates the input for the 'phone' field.
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Only numbers are allowed.")
        return phone

    # Custom validation for the 'date' field to ensure that reservations
    # cannot be made for the past or for today.
    def clean_date(self):
        reservation_date = self.cleaned_data['date']
        if reservation_date < date.today():
            raise ValidationError("Reservation date cannot be in the past.")
        elif reservation_date == date.today():
            raise ValidationError(
                "Reservations can only be made for tomorrow or later."
            )
        return reservation_date
