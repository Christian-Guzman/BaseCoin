from rest_framework import viewsets, permissions
from .models import Transaction, Balance
from django.db.models import Q
from .serializers import TransactionSerializer, UserSerializer, BalanceSerializer
from django.contrib.auth.models import User



## Custom Permissions
class IsOwnerOfTransaction(permissions.BasePermission):
    message = "You must be the source to create a transaction."
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.id == request.data['source']
        return True

   
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class BalanceViewSet(viewsets.ModelViewSet):
    # queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Balance.objects.filter(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer 
    permission_classes = [IsOwnerOfTransaction]

    def get_queryset(self):
        return Transaction.objects.filter(
            Q(source=self.request.user) | Q(destination=self.request.user)
        )
