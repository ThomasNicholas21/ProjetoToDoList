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
        try:
            serializer = ActivitySerializers(data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            mensagem_exception = {
                'error': 'Unexpected error occurred',
                'description': f'{e}'
                }

            if serializer and hasattr(serializer, 'errors') and serializer.errors:
                error = serializer.errors
            else:
                error = mensagem_exception

            return Response(error, status=status.HTTP_400_BAD_REQUEST)   
    

class ActivityApiDetailView(APIView):
    def get(self, *args, **kwargs):
        try:
            activity_id = kwargs.get('activity_id')
            activity = Activity.objects.get(pk=activity_id)
            serializer = ActivitySerializers(activity)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        
        except Activity.DoesNotExist:
            return Response(
                {
                    'error': 'activity not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            return Response(
                {
                    'error': 'Unexpected error occurred',
                    'description': f'{e}'
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self, *args, **kwargs):
        serializer = None 
        
        try:
            activity_id = kwargs.get('activity_id')
            activity = Activity.objects.get(pk=activity_id)
            serializer = ActivitySerializers(activity, data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
                )
        
        except Activity.DoesNotExist:
            return Response(
                {
                    'error': 'activity not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            mensagem_exception = {
                'error': 'Unexpected error occurred',
                'description': f'{e}'
                }

            if serializer and hasattr(serializer, 'errors') and serializer.errors:
                error = serializer.errors
            else:
                error = mensagem_exception

            return Response(error, status=status.HTTP_400_BAD_REQUEST)  
    
    def patch(self, *args, **kwargs):
        return Response(f'PATCH DETAIL ACTIVITY')
    
    def delete(self, *args, **kwargs):
        return Response(f'DELETE DETAIL ACTIVITY')
