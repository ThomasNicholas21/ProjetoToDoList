from django.contrib import admin
from activity.models import Activity

# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'priority'
    list_display_links = 'id',
