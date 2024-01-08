from django.urls import path
from .views import   comment

urlpatterns = [
    
    
    path('comment/<int:pk>/', comment, name='comment'),
    ]