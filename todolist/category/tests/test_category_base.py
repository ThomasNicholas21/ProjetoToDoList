from django.test import TestCase
from activity.models import Category


class CategoryMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(category_name=name)

    def make_category_payload(self):
        return {
            "category_name": "Category test"
        }
    
    def make_updated_payload(self, category):
        return {
            "category_name": str(category)
        }

    def make_category_in_batch(self, amount=10):
        categories = []
        for i in range(amount):
            kwargs = {
                'category_name': f"Category {i}"
            }
            category = self.make_category(**kwargs) 
            categories.append(category)
        return categories


class CategoryMixinTestBase(TestCase, CategoryMixin):
    def setUp(self) -> None:
        return super().setUp()
    