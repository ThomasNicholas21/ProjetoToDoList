from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError
from activity.api.serializer import ActivitySerializers
from activity.models import Activity
# Create your views here.

class ActivityApiView(APIView):
    def get(self, *args, **kwargs):
        try:
            activities = Activity.objects.all()
            serializer = ActivitySerializers(
                activities,
                many=True
            )

            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            return Response(
                {
                    'error': 'Unexpected error occurred',
                    'description': f'{e}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, *args, **kwargs):
        return Response('POST ACTIVITY')
    

class ActivityApiDetailView(APIView):
    def get(self, *args, **kwargs): 
        return Response(f"GET DETAIL ACTIVITY")
    
    def put(self, *args, **kwargs):
        return Response(f'PUT DETAIL ACTIVITY')
    
    def patch(self, *args, **kwargs):
        return Response(f'PATCH DETAIL ACTIVITY')
    
    def delete(self, *args, **kwargs):
        return Response(f'DELETE DETAIL ACTIVITY')
