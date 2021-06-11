<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
import uuid
# Create your models here.

class Signup(models.Model):  
    user_id = models.CharField(primary_key = True,max_length=100)  
    mail_id  = models.CharField(max_length=100)
    password = models.CharField(max_length=20,default='None')
    #password2 = models.CharField(max_length=8)
    class Meta:  
        db_table = "signup"  




>>>>>>> a8d1b39ecf4ea0a8bd1f01783c19247e14f1c514
