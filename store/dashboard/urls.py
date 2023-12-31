from django.urls import path
from .views import  dashboard , delete

urlpatterns = [
    
   path('', dashboard, name='dashboard'),
   path('<int:pk>/delete/', delete, name='delete'),
    
 
]