from django.shortcuts import render,  redirect
from   .forms   import   SignuForm ,    LoginForm
from django.contrib.auth import authenticate, login

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



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the home page or any other desired page
            else:
                # Handle invalid login credentials
                # You may want to display an error message or redirect back to the login page
                pass
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})