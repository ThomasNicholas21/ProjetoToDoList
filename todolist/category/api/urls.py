from django.urls import path
from category.api.views import CategoryApiView, CategoryApiDetailView


app_name='category'


urlpatterns = [
    path('api/category/', CategoryApiView.as_view(), name='category-api'),
    path('api/category/<int:category_id>/', CategoryApiDetailView.as_view(), name='category-detail-api')
]
