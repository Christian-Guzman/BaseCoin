from rest_framework import viewsets, permissions, authentication
from .models import Transaction
from django.db.models import Q
from .serializers import TransactionSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


## Custom Permissions
class IsOwnerOfTransactionOrAdmin(permissions.BasePermission):
    message = "You must be the source to create a transaction and Transactions to self can't be made."
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        elif request.method == 'POST':
            if request.user.id == request.data['source'] and request.user.id == request.data['destination']:
                return False
                
            return not request.data or request.user.id == request.data['source']

        return True

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(username=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer 
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfTransactionOrAdmin]

    def get_queryset(self):
        return Transaction.for_user(self.request.user)
