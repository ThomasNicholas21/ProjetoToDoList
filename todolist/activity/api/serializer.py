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
        status = validated_data.get('status')

        if due_date < timezone.now():
            validated_data['status'] = 'late'

        if status == 'finished':
            validated_data['finished_at'] = timezone.now()

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        categories = validated_data.pop('category', None)
        due_date = validated_data.get('due_date')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if due_date and due_date < timezone.now():
            instance.status = 'late'

        instance.save()

        if categories is not None:
            instance.category.set(categories)

        return instance
