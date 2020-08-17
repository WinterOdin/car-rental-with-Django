from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import *


class createUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'********'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'********'}))
    class Meta:
        model   = User
        fields  = ['username','email', 'password1','password2']
        widgets ={
           
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'John.Doe'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'John.Doe@gmial.com'}),
           
        }
class CustomerUpdate(forms.ModelForm):
    class Meta:
        model   = Customer
        fields  = ['profilePic','name','email','phone']
        widgets = {

            
            'email':forms.TextInput(attrs={'class':'inpBoxCustomer'}),
            'name':forms.TextInput(attrs={'class':'inpBoxCustomer'}),
            'phone':forms.TextInput(attrs={'class':'inpBoxCustomer'}),


        }