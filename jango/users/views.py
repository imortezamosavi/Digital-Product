import random
import uuid

from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        # print(request.data)
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # user, created = User.objects.get_or_create(phone_number=phone_number)
        try:
            user = request.objects.get(phone_number=phone_number)
            return Response({"detail": "User already registered!"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)

        device = Device.objects.create(user=user)

        code = random.randint(100000, 999999)

        # send message (sms or email)
        cache.set(str(phone_number), code, 2*60)

        return Response({'phone_number': phone_number, 'code': code})

        
class GetTokenView(APIView):

    def post(self, requset):
        phone_number = requset.data.get('phone_number')
        code = requset.data.get('code')

        cached_code = cache.get(str(phone_number))

        if code != cached_code:
            return Response(status=status.HTTP_403_FORBIDDEN)
        

        token = str(uuid.uuid4())

        return Response({'token':token})
























