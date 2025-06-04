from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'category_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'created_at', 'updated_at',
        ]
