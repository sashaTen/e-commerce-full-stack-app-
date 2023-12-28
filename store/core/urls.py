from django.urls import path
from .views import   index ,    contact ,  signup   ,  login_view ,  logout_view

urlpatterns = [
    
    path('',index, name='index'),
    path('contact/'  ,  contact, name=  'contact'),
    path('signup/' ,    signup ,    name='signup'),
    path('login/' ,  login_view ,   name='login'), 
    path('logout/' ,    logout_view ,   name='logout'),
    
 
]