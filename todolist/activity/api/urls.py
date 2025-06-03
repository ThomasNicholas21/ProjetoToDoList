from django.urls import path
from activity.api.views import ActivityApiView


app_name='activity'


urlpatterns = [
    path('api/activity/', ActivityApiView.as_view(), name='activity-api')
]
