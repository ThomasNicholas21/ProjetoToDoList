from django.urls import path
from activity.api.views import ActivityApiView, ActivityApiDetailView


app_name='activity'


urlpatterns = [
    path('api/activity/', ActivityApiView.as_view(), name='activity-api'),
    path('api/activity/<int:activity_id>/', ActivityApiDetailView.as_view(), name='activity-detail-api')
]
