from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from subscriptions.models import Subscription, Package

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer

# Create your views here.
class CategoryListView(APIView):


    def get(self, request):
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True, context= {'request':request})
        return Response(serializer.data)

class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            product = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(product, context= {'request':request})
        return Response(serializer.data)

class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        print(request.auth)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context= {'request':request})
        return Response(serializer.data)

class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if not Subscription.objects.filter(
            user = request.uesr,
            expire_time__gt = timezone.now()
        ).exists():
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context= {'request':request})
        return Response(serializer.data)
    
class FileListView(APIView):


    def get(self, request, product_pk):
        files = File.objects.filter(product_id=product_pk)
        serializer = FileSerializer(files, many=True, context= {'request':request})
        return Response(serializer.data)

class FileDetailView(APIView):

    def get(self, request, product_pk, pk):
        try:
            file = File.objects.get(pk=pk, product_id=product_pk)
        except File.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(file, context= {'request':request})
        return Response(serializer.data)


