from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ActivityApiView(APIView):
    def get(self, *args, **kwargs):
        return Response('GET ACTIVITY')
    
    def post(self, *args, **kwargs):
        return Response('POST ACTIVITY')
    

class ActivityApiDetailView(APIView):
    def get(self, *args, **kwargs): 
        return Response(f"GET DETAIL ACTIVITY")
