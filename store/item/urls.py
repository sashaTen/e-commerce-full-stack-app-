# urls.py

from django.urls import path
from .views import index_item, detail, category,   new  ,  edit    ,  item_search

urlpatterns = [
    path('', index_item, name='item'),
    path('<int:pk>/', detail, name='detail'),
    path('/<int:pk>/', category, name='category'),
    path('new/' ,    new    ,     name='new'),
    path('/edit/<int:pk>/', edit, name='edit'),
    path('search/', item_search, name='item_search'),
    
    # ... other URL patterns if any
]
