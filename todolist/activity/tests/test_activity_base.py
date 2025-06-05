from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from activity.models import Activity, Category, User
import random


class ActivityMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(category_name=name)

    def make_user(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_activity(
        self,
        user_data=None,
        title='Activity Title',
        description='Activity Description',
        due_date=timezone.make_aware(datetime(year=2025, month=12, day=30)),
        category_data=None,
        status='in_progress',
        priority='low',
        finished_at=None,
    ):
        if user_data is None:
            user_data = {}

        if category_data is None:
            category_data = {}

        user = self.make_user(**user_data)
        category = self.make_category(**category_data)

        activity = Activity.objects.create(
            user=user,
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            priority=priority,
            finished_at=finished_at,
        )

        activity.category.set([category])

        return activity
    
    def make_activity_payload(self):
        user = self.make_user()
        category = self.make_category()

        return {
            "user": user.id,
            "title": "Título da Atividade",
            "description": "Descrição de teste",
            "due_date": timezone.make_aware(datetime(year=2025, month=12, day=30)),
            "status": "in_progress",
            "priority": "low",
            "category": [category.id]
        }
    
    def make_updated_payload(self, activity):
        category = self.make_category()
        return {
            "title": "Atualizado",
            "description": "Atualizado",
            "due_date": "2025-12-30T00:00:00Z",
            "status": "in_progress",
            "priority": "high",
            "user": activity.user.id,
            "category": [category.id]
        }

    
    def make_activity_in_batch(self, amount=10):
        activities = []
        status_list = ['in_progress', 'late', 'finished']
        priority_list = ['low', 'medium', 'high']
        for i in range(amount):
            kwargs = {
                'user_data': {'username': f'u{i}'},
                'title': f'Activity Title {i}',
                'description': f'description {i}',
                'due_date': timezone.make_aware(datetime(year=2025, month=12, day=30)),
                'status': random.choice(status_list),
                'priority': random.choice(priority_list),
                'finished_at': None
            }
            activity = self.make_activity(**kwargs)
            activities.append(activity)
        return activities


class ActivityMixinTestBase(TestCase, ActivityMixin):
    def setUp(self) -> None:
        return super().setUp()
