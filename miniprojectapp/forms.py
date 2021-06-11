<<<<<<< HEAD
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
=======
from django import forms  
from miniprojectapp.models import Signup 
from django.contrib.auth.hashers import check_password 
  
class SignupForm(forms.ModelForm):  
	user_id = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'} ))
	mail_id  = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email Address','class':'form-control'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
	confirm_password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class':'form-control'}))
	class Meta:
		model=Signup
		fields="__all__"
	def clean(self):
		cleaned_data=super().clean()
		p1=self.cleaned_data['password']
		p2=self.cleaned_data['confirm_password']
		if p1!=p2:
			raise forms.ValidationError('Password doesnt match')
	#	if not check_password(confirm_password,self.instance.password):
	#		self.add_error('confirm_password','Password doesnt match')

    
>>>>>>> a8d1b39ecf4ea0a8bd1f01783c19247e14f1c514
