from django.shortcuts import render ,    get_object_or_404
from .models   import  CommentModel
from item.models  import   Item
from .forms  import   CommentForm
from   django.contrib.auth.decorators   import login_required

# Create your views here.

@login_required
def comment(request, pk):
    item = get_object_or_404(Item, pk=pk)
    comments = CommentModel.objects.filter(item=item)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.item = item
            comment.save()
    else:
        form = CommentForm()

    return render(request, "comment.html", {'item': item, 'comments': comments, 'form': form})




def post( request):
        new_comment = CommentModel(text=request.POST.get('text'),
                                  author=User)
        new_comment.save()
      