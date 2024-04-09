from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reviews.models import Review
from datetime import datetime

class ReviewListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user and reviews for testing
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        Review.objects.create(title="Test Review 1", content="Test Content 1", user=test_user, approved=True)
        Review.objects.create(title="Test Review 2", content="Test Content 2", user=test_user2, approved=False)

    def test_review_list_view_with_no_login(self):
        """
        Test that only approved reviews are shown to unauthenticated users.
        """
        response = self.client.get(reverse('reviews:review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('reviews' in response.context)
        self.assertEqual(len(response.context['reviews']), 1)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_review_list_view_with_login(self):
        """
        Test that authenticated users can see their own unapproved reviews in addition to the approved ones.
        """
        self.client.login(username='testuser2', password='12345')
        response = self.client.get(reverse('reviews:review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('reviews' in response.context)
        self.assertEqual(len(response.context['reviews']), 2)