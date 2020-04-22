from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



def is_positive(value):
  if value <= 0:
    raise ValidationError("Amount has to be greater than 0")

def get_user_balance(user):
        balance = 0
        for t in Transaction.for_user(user):
            if t.source == user:
                balance -= t.amount
            else:
                balance += t.amount
        return balance
  

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

    def clean(self):
      balance = get_user_balance(self.request.user)
      if self.amount > balance:
        raise ValidationError("Insufficient Funds")

    @staticmethod
    def for_user(user):
        return Transaction.objects.filter(
            Q(source=user) | Q(destination=user)
        )

    def __str__(self):
      return (f'Source: {self.source}, Destination: {self.destination}, Amount: {self.amount}')
    
