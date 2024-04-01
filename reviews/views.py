from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import Review
from .forms import ReviewForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def review_list(request):
    if request.user.is_authenticated:
        reviews_list = Review.objects.filter(Q(approved=True) | Q(user=request.user)).distinct().order_by('-created_at')
    else:
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


@login_required
def review_update(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.approved = False
            review.save()
            return redirect('reviews:review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_edit.html', {'form': form})


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('reviews:review_list')