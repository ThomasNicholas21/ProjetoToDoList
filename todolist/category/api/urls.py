from django.urls import path
from .views import TesteViewTesteAPI


urlpatterns = [
    path('testeteste/', TesteViewTesteAPI.as_view(), name='teste-api')
]
