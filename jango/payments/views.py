import requests
import uuid

from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from subscriptions.models import Subscription, Package

from .models import Gateway, Payment
from .serializers import GatewaySerializer, PaymentSerializer


# Create your views here.
class GatewayViews(APIView):
    def get(self, request):
        gateways = Gateway.objects.filter(is_enable=True)
        serializer = GatewaySerializer(gateways, many=True)
        return Response(serializer.data)
    

class PaymentViews(APIView):
    permission_classes = [IsAuthenticated]  # Corrected attribute name

    def get(self, request):
        gateway_id = request.query_params.get('gateway')
        package_id = request.query_params.get('package')

        try:
            gateway = Gateway.objects.get(id=gateway_id, is_enable=True)
            package = Package.objects.get(id=package_id, is_enable=True)
        except (Package.DoesNotExist, Gateway.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        payment = Payment.objects.create(
            user=request.user,  # Corrected attribute name
            package=package,
            gateway=gateway,
            price=package.price,
            phone_number=request.user.phone_number,  # Corrected attribute name
            token=str(uuid.uuid4())
        )

        return Response({'token': payment.token, 'callback_url': ''})


    def post(self, request):
        token = request.data.get('token')
        status = request.data.get('status')

        try:
            payment = Payment.objects.get(token=token)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if status != '10':  # Corrected status comparison
            payment.status = Payment.STATUS_CANCELED
            payment.save()

            return Response({'detail': 'Payment Canceled By User.'}, status=status.HTTP_400_BAD_REQUEST)
        
        r = requests.post('bank_verify_url', data={})
        if r.status_code // 100 != 2:
            payment.status = Payment.STATUS_ERROR
            payment.save()

            return Response({'detail': 'Payment Verification Failed.'}, status=status.HTTP_400_BAD_REQUEST)
        

        payment.status = Payment.STATUS_PAID
        payment.save()

        Subscription.objects.create(
            user=payment.user,  # Corrected attribute name
            package=payment.package,  # Corrected attribute name
            expire_time=timezone.now() + timezone.timedelta(days=payment.package.duration.days)  # Corrected attribute name
        )

        return Response({'detail': 'Payment Is Successful.'})