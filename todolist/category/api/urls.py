from django.urls import path
from category.api.views import CategoryApiView


app_name='category'


urlpatterns = [
    path('api/category/', CategoryApiView.as_view(), name='category-api')
]
