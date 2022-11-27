from django import forms
from .models import User

class UserForm(forms.ModelForm): 
    
    email = forms.CharField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs= {'class' : 'form-control'}))

    class Meta():
        model = User       
        fields = ('email','password')