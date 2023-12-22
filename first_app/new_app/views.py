import json

from rest_framework.response import Response
from rest_framework.views import APIView

from .producer import publish


# Create your views here.

class myDataView(APIView):

    def get(self, request):
        data = request.data
        # print("hello")
        files = request.FILES
        f = files["file"].file
        content = f.read()
        my_json = content.decode('utf-8')
        ff = json.loads(my_json)
        for i in ff:
            publish("share_details", i)
        return Response({"hello": ff})