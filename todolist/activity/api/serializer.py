from rest_framework import serializers
from django.utils import timezone
from activity.models import Activity


class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'id', 'user', 'title',
            'description', 'due_date',
            'category', 'status',
            'priority', 'finished_at',
            'created_at', 'updated_at',
        ]
        read_only_fields = [
            'created_at', 'updated_at',
        ]

    def create(self, validated_data):
        due_date = validated_data.get('due_date')

        if due_date < timezone.now():
            validated_data['status'] = 'late'

        return super().create(validated_data)
