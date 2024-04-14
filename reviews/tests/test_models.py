from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from reviews.models import Review


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up a user and review for all tests
        """
        test_user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        Review.objects.create(
            user=test_user,
            title='Test Review',
            content='This is a test review content.',
            rating=5
        )

    def test_review_string_representation(self):
        """
        Test the string representation of the Review model
        """
        review = Review.objects.get(id=1)
        expected_representation = (
            f'{review.title} | written by {review.user}'
        )
        self.assertEqual(str(review), expected_representation)

    def test_review_defaults(self):
        """
        Check if the 'approved' field of a new review defaults to False
        """
        review = Review.objects.get(id=1)
        self.assertFalse(
            review.approved, "Review should not be approved by default."
        )

    def test_review_rating_range(self):
        """
        Ensure that the rating for a review falls within the
        acceptable range (1 to 10)
        """
        review = Review.objects.get(id=1)
        self.assertTrue(
            1 <= review.rating <= 10,
            "Review rating should be between 1 and 10."
        )
