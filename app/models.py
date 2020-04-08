from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



def is_positive(value):
  if value <= 0:
    raise ValidationError("Amount has to be greater than 0")
  

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
    amount = models.PositiveIntegerField(validators=[is_positive])


    @staticmethod
    def for_user(user):
        return Transaction.objects.filter(
            Q(source=user) | Q(destination=user)
        )

    def __str__(self):
      return (f'Source: {self.source}, Destination: {self.destination}, Amount: {self.amount}')


