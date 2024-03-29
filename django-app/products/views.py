from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product,User
from .serializers import ProductSerializer

import random
# Create your views here.
from .producer import publish


class ProductViewSet(viewsets.ViewSet):
    def list(self,request): #/api/products get
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

    def create(self,request): #/api/products post
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created',serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retreive(self,requests,pk=None):#/api/products/<str-id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self,requests,pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product,data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self,requests,pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self,_):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id,
        })


