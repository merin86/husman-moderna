from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from .models import Review
from .forms import ReviewForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def review_list(request):
    """
    Display reviews to users. If the user is authenticated,
    they will see all approved reviews plus their own unapproved reviews.
    Otherwise, only approved reviews are shown.
    Pagination is implemented to organize the display of reviews.
    """
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
    """
    Allow logged-in users to create a new review.
    Reviews must be approved by an admin before becoming
    visible to other users. A success message is displayed
    upon submission.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been submitted and is awaiting approval.")
            return redirect('reviews:review_list')
    else:
        form = ReviewForm()
    return redirect('reviews:review_list')


@login_required
def review_update(request, review_id):
    """
    Enable users to update their existing reviews.
    The updated review requires reapproval from an admin.
    An informational message is displayed after submission
    indicating the review is pending approval.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.approved = False
            review.save()
            messages.info(request, "Your review has been updated and is awaiting reapproval.")
            return redirect('reviews:review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_edit.html', {'form': form})


@login_required
def review_delete(request, review_id):
    """
    Provide a way for users to delete their reviews.
    A success message confirms the deletion. Users are
    redirected to the list of reviews afterward.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, "Your review has been successfully deleted.")
    return redirect('reviews:review_list')