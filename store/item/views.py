from django.shortcuts import render

# Create your views here.
def     index_item(request):
    return  render(request ,   'item.html' )