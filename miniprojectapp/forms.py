from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

my_default_errors = {
    'invalid': 'Enter a valid email id'
}
class SignUpForm(UserCreationForm):
	username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'} ))
	email  = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email Address','class':'form-control'}),error_messages=my_default_errors)
	password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
	password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class':'form-control'}))
	class Meta:
		model=User
		fields=('username','email','password1','password2')
