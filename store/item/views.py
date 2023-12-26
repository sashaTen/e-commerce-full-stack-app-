from django.shortcuts import render  ,get_object_or_404
from .models import Category, Item

def index_item(request):
    # Retrieve data from the models
    categories = Category.objects.all()
    items = Item.objects.all()

    # Pass the data to the template
    context = {
        'categories': categories,
        'items': items,
    }

    # Render the template with the data
    return render(request, 'item.html', context)



def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'detail.html', {'item': item})




def   category(request ,    pk):
    category_object   =     get_object_or_404(Category ,    pk=pk)
    return  render(request ,     'category_page.html' ,     {"category"  :   category_object})


