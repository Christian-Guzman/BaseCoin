from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from app.views import TransactionViewSet, UserViewSet, BalanceViewSet 
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'user')
router.register('transactions', TransactionViewSet, 'transaction')
router.register('balances', BalanceViewSet, 'balance')


urlpatterns = [
    path("", include(router.urls)),
    path("token/", obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
