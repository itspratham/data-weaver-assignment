import json
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductView(APIView):

    def get(self, request, pk=None):
        try:
            if pk:
                x = requests.get('http://127.0.0.1:8000/api/products/{}'.format(pk))
                print(x.content)
                return Response({"data": str(json.loads(x.content))}, status=status.HTTP_200_OK)
            else:
                x = requests.get('http://127.0.0.1:8000/api/products')
                print(x.content)
                return Response(data={"data": str(json.loads(x.content))}, status=status.HTTP_200_OK)
        except:
            return Response(data={"error occured while retrieving data"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            x = requests.post('http://127.0.0.1:8000/api/products', data=request.data)
            print(x.content)
            return Response({"data": str(json.loads(x.content))}, status=status.HTTP_200_OK)
        except:
            return Response(data={"error occured while retrieving data"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            x = requests.put('http://127.0.0.1:8000/api/products/{}'.format(pk), data=request.data)
            print(x.content)
            return Response({"data": str(json.loads(x.content))}, status=status.HTTP_200_OK)
        except:
            return Response(data={"error occured while retrieving data"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            x = requests.delete('http://127.0.0.1:8000/api/products/{}'.format(pk))
            print(x.content)
            return Response({"data": str(json.loads(x.content))}, status=status.HTTP_200_OK)
        except:
            return Response(data={"error occured while retrieving data"}, status=status.HTTP_400_BAD_REQUEST)


class CalculateScore(APIView):
    def get(self, request):
        try:
            x = requests.get('http://127.0.0.1:8000/api/products/score')
            print(x.content)
            return Response({"data": json.loads(x.content)}, status=status.HTTP_200_OK)
        except:
            return Response(data={"error occured while retrieving data"}, status=status.HTTP_400_BAD_REQUEST)
