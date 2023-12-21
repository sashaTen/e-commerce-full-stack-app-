from django.urls import path
from .views import  index_item

urlpatterns = [
    
    
    path(''  ,  index_item, name=  'item')
 
]