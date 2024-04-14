from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    The form for creating and editing a review
    """
    rating = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'rating-input',
                'min': '1',
                'max': '10'
            }
        )
    )

    class Meta:
        """
        Meta options for ReviewForm.
        """
        model = Review
        fields = ['title', 'content', 'rating']
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'content-textarea'}
            ),
        }

    def clean_title(self):
        """
        Custom clean method for the 'title' field to ensure
        it's not just whitespace.
        """
        title = self.cleaned_data.get('title').strip()
        if not title:
            raise forms.ValidationError("This field cannot be blank.")
        return title

    def clean_content(self):
        """
        Custom clean method for the 'content' field to ensure
        it's not just whitespace.
        """
        content = self.cleaned_data.get('content').strip()
        if not content:
            raise forms.ValidationError("This field cannot be blank.")
        return content
