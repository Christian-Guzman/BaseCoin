from .models import Transaction, Balance
from django.contrib.auth.models import User
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):

  class Meta:
    model = Transaction
    fields = ['source', 'destination', 'amount']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class BalanceSerializer(serializers.ModelSerializer):

  # total = serializers.SerializerMethodField('get_total')

  class Meta:
    model = Balance
    fields = ['total', 'user']

  # def get_total(self, obj):
  #     money_out = obj.user.transaction.amount

  #   elif obj.user.id == transaction.destination:
  #     money_in = obj.user.transaction.amount

  #   total = money_in - money_out
