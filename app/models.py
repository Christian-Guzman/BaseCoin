from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    source = models.ForeignKey(User, 
      related_name="outgoing_transactions",
      related_query_name="outgoing_transaction",
      on_delete=models.PROTECT
    )
    destination = models.ForeignKey(User,
        related_name="incoming_transactions",
        related_query_name="incoming_transaction",
        on_delete=models.PROTECT
    )
    amount = models.IntegerField()

    def __str__(self):
      return (f'Source: {self.source}, Destination: {self.destination}, Amount: {self.amount}')

class Balance(models.Model):
  total = models.IntegerField(default=0)
  user = models.ForeignKey(User, on_delete=models.PROTECT)

