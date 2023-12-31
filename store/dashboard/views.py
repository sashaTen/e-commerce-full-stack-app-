from django.shortcuts import render  ,get_object_or_404  , redirect
from item.models   import    Item
from django.contrib.auth.decorators   import   login_required 
# Create your views here.
@login_required
def    dashboard(request):
    items   =    Item.objects.filter(created_by = request.user)

    return    render(request  ,    'dashboard.html' ,  {"items"  :   items})




@login_required
def   delete(request  ,   pk):
    item  =  get_object_or_404(Item ,  pk=pk ,  created_by=  request.user)
    item.delete()
    return   redirect('/dashboard/')
