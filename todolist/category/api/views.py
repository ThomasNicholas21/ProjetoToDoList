from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from category.models import Category
from category.api.serializer import CategorySerializer

# Create your views here.

class CategoryApiView(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class CategoryApiDetailView(APIView):
    ...
