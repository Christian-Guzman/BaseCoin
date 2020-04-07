from rest_framework.test import APITestCase
from .models import Transaction
from django.contrib.auth.models import User

# Create your tests here.
class TestUsersCanOnlySeeTheirTransactions(APITestCase):
    def setUp(self):
        self.source =  User.objects.create(username="source")
        self.destination =  User.objects.create(username="destination")
        self.not_involved =  User.objects.create(username="not_involved")

        self.t = Transaction.objects.create(source=self.source,destination=self.destination,amount=30)

    def test_not_involved_user_cannot_see_other_transactions(self):
        self.client.force_authenticate(self.not_involved)

        response = self.client.get('/transactions/')

        self.assertEqual(response.data, [])

    def test_source_can_see_the_transaction(self):
        self.client.force_authenticate(self.source)

        response = self.client.get('/transactions/')

        self.assertEqual(len(response.data),1)

    def test_destination_can_see_the_transaction(self):
        self.client.force_authenticate(self.destination)

        response = self.client.get('/transactions/')

        self.assertEqual(len(response.data),1)
