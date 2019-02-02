from django.http import HttpResponse
from .forms import LoginForm
from .login2 import NameForm
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the showdata index.")

def sindex(request):
    return HttpResponse("Hello, world. You're at the  second showdata index.")

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = Loginform()
		
   return render(request, 'loggedin.html', {"username" : username})

def testLogin(request):
  if request.method == "POST":
    form = NameForm(request.POST)
    if form.is_valid():
     subject = form.cleaned_data['subject']
     return render(request, 'loggedin.html', {"username" : subject})
  else:
    form = NameForm()
  return render(request, 'login2.html', {"form" : form})

def login2html(request):
  form = NameForm()
  return render(request, 'login2.html', {"form" : form})

