<<<<<<< HEAD
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


=======
from django.shortcuts import render
from miniprojectapp.forms import SignupForm
from django.http import HttpResponse  
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,  authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.  
def index(request):  
    stu = SignupForm()
    if request.method=="POST":
        stu = SignupForm(request.POST)  
        if stu.is_valid():
            stu.save()
            stu = SignupForm()
            
        else:
            messages.warning(request,'Something went wrong.')
            stu = SignupForm()
    return render(request,"index.html",{'form':stu})  
def demo(request):
	render(request,"demo.html")
>>>>>>> a8d1b39ecf4ea0a8bd1f01783c19247e14f1c514
