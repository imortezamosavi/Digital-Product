import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Package, Subscription
from .serializers import PackageSerializer, SubscriptionSerializer
# Create your views here.
class PackageViews(APIView):
    def get(self, request):
        packages = request.objects.filter(is_enable=True)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)
    
class SubscriptionViews(APIView):
    Permission_class = [IsAuthenticated]

    def get(self, request):
        subscriptions = request.objects.filter(
            user = request.uesr,
            expire_time__gt = timezone.now()
        )
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)