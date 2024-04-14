from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from datetime import date, time
from reservations.models import Reservation


class ReservationViewsTest(TestCase):
    def setUp(self):
        """
        Set up user for tests
        """
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.reservation = Reservation.objects.create(
            user=self.user,
            date=date.today(),
            time=time(18, 0),  # 6:00 PM
            guests=4,
            first_name='Martin',
            last_name='Liljenroth',
            phone='123456789',
            email='martinliljenroth@example.com',
            message='Test message'
        )

    def test_book_reservation_view(self):
        """
        Test access to book reservation view
        """
        response = self.client.get(
            reverse('reservations:book_reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'reservations/book_reservation.html')

    def test_my_reservations_view(self):
        """
        Test access to my reservations view
        """
        response = self.client.get(
            reverse('reservations:my_reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'reservations/my_reservations.html')
        self.assertIn('reservations', response.context)

    def test_edit_reservation_view(self):
        """
        Test access to edit reservation view
        """
        response = self.client.get(
            reverse('reservations:edit_reservation',
                    kwargs={'reservation_id': self.reservation.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'reservations/book_reservation.html')

    def test_delete_reservation_view(self):
        """
        Test delete reservation view
        """
        response = self.client.post(
            reverse('reservations:delete_reservation',
                    kwargs={'pk': self.reservation.pk}))
        self.assertRedirects(
            response, reverse('reservations:my_reservations'))
        self.assertFalse(
            Reservation.objects.filter(pk=self.reservation.pk).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "The reservation has been successfully deleted.")

    def test_large_reservation_view(self):
        """
        Test access to large reservation view
        """
        response = self.client.get(
            reverse('reservations:large_reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'reservations/large_reservation.html')
