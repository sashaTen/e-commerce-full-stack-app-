from django.shortcuts import render,  redirect
from   .forms   import   SignuForm

# Create your views here.
def index(request):
  return  render(request  ,   "index.html")    


def   contact(request):
  return  render(request ,    "contact.html")



def   signup(request):
  if  request.method == 'POST':
    form =  SignuForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/login/')
  else :  
   form =    SignuForm()
  return  render(request  ,   "signup.html"   ,   {"form":form})