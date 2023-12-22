import sys
import sys
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, SKU
from .serializers import ProductSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView




class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Create your views here.


class CalculateScore(APIView):
    def get(self, request):
        f = SKU.objects.all().count()
        f1 = SKU.objects.filter(stock="In Stock").count()
        f2 = f1 / f
        print("f2", "ttttttt", f)
        return Response(data={"score": f2}, status=status.HTTP_200_OK)
