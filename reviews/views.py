from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def review_list(request):
    reviews_list = Review.objects.filter(approved=True).order_by('-created_at')
    paginator = Paginator(reviews_list, 3)

    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

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