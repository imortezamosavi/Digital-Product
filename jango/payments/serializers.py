from rest_framework import serializers

from .models import Gateway, Payment

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('title', 'description', 'avatar', 'created_time', 'updated_time')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user', 'package', 'gateway', 'price', 'status', 'phone_number', 'consumed_code', 'created_time', 'updated_time')