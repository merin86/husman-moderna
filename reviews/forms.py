from django import forms
from .models import Review
from django.core.validators import MinValueValidator, MaxValueValidator

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'rating-input', 'min': '1', 'max': '10'}))

    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'content-textarea'}),
        }