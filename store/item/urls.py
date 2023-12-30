# urls.py

from django.urls import path
from .views import index_item, detail, category,   new 

urlpatterns = [
    path('', index_item, name='item'),
    path('<int:pk>/', detail, name='detail'),
    path('/<int:pk>/', category, name='category'),
    path('new/' ,    new    ,     name='new'),
    
    # ... other URL patterns if any
]
