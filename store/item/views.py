from django.shortcuts import render  ,get_object_or_404  , redirect
from .models import Category, Item
from   django.contrib.auth.decorators   import login_required
from    .forms  import    NewItemForm


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



@login_required
def    new(request):
    if request.method ==  'POST' :
        form =   NewItemForm(request.POST ,  request.FILES)
        if  form.is_valid():
            item = form.save(commit=False)
            item.created_by   =  request.user
            item.save()
            return  redirect('detail'  ,  pk=item.id)
    form   =   NewItemForm
    return   render(request ,    'form.html' ,  {'form' : form})


