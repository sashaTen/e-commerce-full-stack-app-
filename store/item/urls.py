# urls.py

from django.urls import path
from .views import index_item, detail, category

urlpatterns = [
    path('', index_item, name='item'),
    path('<int:pk>/', detail, name='detail'),
    path('/<int:pk>/', category, name='category'),
    # ... other URL patterns if any
]
