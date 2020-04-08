from .models import Transaction
from django.contrib.auth.models import User
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = ['source', 'destination', 'amount']

    def get_balance(self, user):
        balance = 0
        for t in Transaction.for_user(user):
            if t.source == user:
                balance -= t.amount
            else:
                balance += t.amount
        return balance
        

        

class UserSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', "balance"]
    

    def get_balance(self, user):
        balance = 0
        for t in Transaction.for_user(user):
            if t.source == user:
                balance -= t.amount
            else:
                balance += t.amount
        return balance