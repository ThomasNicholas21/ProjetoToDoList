from django.contrib import admin
from category.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'category_name',
    list_display_links = 'id',
