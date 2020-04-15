from .models import Transaction, get_user_balance
from django.contrib.auth.models import User
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['source', 'destination', 'amount']
        
    def validate(self, data):
        if data['amount'] > get_user_balance(data['source']):
            raise serializers.ValidationError("Insufficient Funds")
        return super().validate(data) 
    
        

class UserSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', "balance"]
    

    def get_balance(self, user):
        return get_user_balance(user)