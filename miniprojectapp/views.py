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
            messages.success(request,'Account created.. Please login')
        else:
            messages.warning(request,'Something went wrong.')
    return render(request,"index.html",{'form':stu})  
