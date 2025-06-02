from django.urls import path
from .views import TesteViewAPI

urlpatterns = [
    path('teste/', TesteViewAPI.as_view(), name='teste-api')
]
