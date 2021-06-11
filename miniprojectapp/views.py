from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login as dj_login
from miniprojectapp.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def signup(request):
    form=SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form=SignUpForm()
            return redirect('/login/')
        else:
            form = SignUpForm()
    return render(request, 'index.html', {'form': form})
def login1(request):
    return render(request,"login.html")
def login2(request):

    if request.method=="POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            dj_login(request, user)
            messages.success(request, "Logged in successfully!")
            return HttpResponse('Success')
    #return render(request, 'login.html')
    #return HttpResponse('Hello')


