from rest_framework import serializers

from .models import Gateway, Payment

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('title', 'sku', 'description', 'avatar', 'price', 'duration')

class PaymentSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Payment
        fields = ('package', 'created_time', 'expire_time')