from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.

class Activity(models.Model):
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activity'
    )
    title = models.CharField(
        max_length=128
    )
    description = models.TextField()
    due_date = models.DateTimeField()
    category = models.ManyToManyField(
        Category,
        blank=True
    )
    status = models.CharField(
        max_length=15,
        choices=(
            ('in_progress', 'In progress'),
            ('late', 'Late'),
            ('finished', 'Finished'),
        ),
        default='in_progress'
    )
    priority = models.CharField(
        max_length=15,
        choices=(
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        )
    )
    finished_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
