from django import forms
from .models import Review
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# The form for creating and editing a review
class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'rating-input', 'min': '1', 'max': '10'}))

    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'content-textarea'}),
        }

    # Custom clean method for the 'title' field to ensure it's not just whitespace.
    def clean_title(self):
        title = self.cleaned_data.get('title').strip()
        if not title:
            raise forms.ValidationError("This field cannot be blank.")
        return title

    # Custom clean method for the 'content' field to ensure it's not just whitespace.
    def clean_content(self):
        content = self.cleaned_data.get('content').strip()
        if not content:
            raise forms.ValidationError("This field cannot be blank.")
        return content