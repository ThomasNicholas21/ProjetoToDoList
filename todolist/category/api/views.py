from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from category.models import Category
from category.api.serializer import CategorySerializer

# Create your views here.

class CategoryApiView(APIView):
    def get(self, *args, **kwargs):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)

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
            serializer = CategorySerializer(data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            return Response(
                {
                    'error': 'Unexpected error occurred',
                    'description': f'{e}'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class CategoryApiDetailView(APIView):
    def get(self, *args, **kwargs):
        try:
            category_id = kwargs.get('category_id')
            category = Category.objects.get(pk=category_id)
            serializer = CategorySerializer(category)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        
        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'category not found.'
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
            category_id = kwargs.get('category_id')
            category = Category.objects.get(pk=category_id)
            serializer = CategorySerializer(category, data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'category not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            return Response(
                {
                    'error': 'Unexpected error occurred',
                    'description': f'{e}'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def patch(self, *args, **kwargs):
        serializer = None

        try:
            category_id = kwargs.get('category_id')
            category = Category.objects.get(pk=category_id)
            serializer = CategorySerializer(category, data=self.request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        
        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'category not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            return Response(
                {
                    'error': 'Unexpected error occurred',
                    'description': f'{e}'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def delete(self, *args, **kwargs):
        try:
            category_id = kwargs.get('category_id')
            category = Category.objects.get(pk=category_id)
            category.delete()

            return Response(
                {
                    'success': 'category deleted'
                },
                status=status.HTTP_204_NO_CONTENT
            )
        
        except Category.DoesNotExist:
            return Response(
                {
                    'error': 'category not found.'
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
        