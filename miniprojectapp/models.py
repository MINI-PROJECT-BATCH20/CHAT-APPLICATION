from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
import uuid
# Create your models here.

class Signup(models.Model):  
    user_id = models.CharField(max_length=40)  
    mail_id  = models.CharField(max_length=100)
    """password1 = models.CharField(max_length=8)
    password2 = models.CharField(max_length=8)"""
    class Meta:  
        db_table = "signup"  




