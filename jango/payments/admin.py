from django.contrib import admin
from .models import Gateway, Payment

# Register your models here.

@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'description', 'created_time', 'updated_time']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'price', 'getway', 'status', 'phone_number', 'device_uuid', 'consumed_code', 'created_time', 'updated_time']
    list_filter = ['status', 'getway', 'package']
    search_fields = ['uesr__name', 'phone_number']