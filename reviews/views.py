from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def review_list(request):
    reviews = Review.objects.filter(approved=True)
    form = ReviewForm()
    return render(request, 'reviews/reviews.html', {'reviews': reviews, 'form': form})

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:review_list')
    else:
        form = ReviewForm()
    return redirect('reviews:review_list')