from rest_framework import serializers
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
