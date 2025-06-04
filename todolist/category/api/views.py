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
        serializer = CategorySerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class CategoryApiDetailView(APIView):
    ...
