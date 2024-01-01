# urls.py

from django.urls import path
from .views import index_item, detail, category,   new  ,  edit

urlpatterns = [
    path('', index_item, name='item'),
    path('<int:pk>/', detail, name='detail'),
    path('/<int:pk>/', category, name='category'),
    path('new/' ,    new    ,     name='new'),
    path('/<int:pk>/edit/', edit, name='edit'),
    
    # ... other URL patterns if any
]
