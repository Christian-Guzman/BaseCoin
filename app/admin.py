from django.contrib import admin
from .models import Transaction, Balance

admin.site.register(Transaction)
admin.site.register(Balance)