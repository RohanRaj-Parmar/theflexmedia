from django.contrib import admin
from .models import CustomerRequest

@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'email', 'phone', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    date_hierarchy = 'created_at'