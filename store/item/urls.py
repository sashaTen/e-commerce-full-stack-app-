from django.urls import path
from .views import  index_item ,  detail

urlpatterns = [
    
    
    path(''  ,  index_item, name=  'item'),
    path('<int:pk>/'   , detail   ,  name="detail" )
 
]