from rest_framework import viewsets, permissions
from .models import Transaction
from django.db.models import Q
from .serializers import TransactionSerializer, UserSerializer
from django.contrib.auth.models import User



## Custom Permissions
class IsOwnerOfTransaction(permissions.BasePermission):
    message = "You must be the source to create a transaction."
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.id == request.data['source']
        return True

class IsSelfOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if view.action == 'retrieve':
            return view.kwargs['pk'] == str(request.user.id)

        return False
   
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    This is a docstring
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrAdmin]

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer 
    permission_classes = [permissions.IsAdminUser | IsOwnerOfTransaction]

    def get_queryset(self):
        return Transaction.for_user(self.request.user)

