from django.urls import path
from category.api.views import TesteViewTesteAPI


urlpatterns = [
    path('testeteste/', TesteViewTesteAPI.as_view(), name='teste-api')
]
