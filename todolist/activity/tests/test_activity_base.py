from django.test import TestCase
from datetime import datetime
from activity.models import Activity, Category, User


class ActivityMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

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
        due_data=datetime(year=2025, month=12, day=30),
        category_data=None,
        status='in_progress',
        priority='low',
        finished_at=None,
    ):
        if user_data is None:
            user_data = {}

        if category_data is None:
            category_data = {}

        return Activity.objects.create(
            user=self.make_user(**user_data),
            title=title,
            description=description,
            due_data=due_data,
            category_data=self.make_category(**category_data),
            status=status,
            priority=priority,
            finished_at=finished_at,
        )


class ActivityMixinTestBase(TestCase, ActivityMixin):
    def setUp(self) -> None:
        return super().setUp()
    