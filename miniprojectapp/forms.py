from django import forms  
from miniprojectapp.models import Signup  
  
class SignupForm(forms.ModelForm):  
	user_id = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'USERID'}))
	mail_id  = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'MAILID'}))
	class Meta:
		model=Signup
		fields="__all__"
    