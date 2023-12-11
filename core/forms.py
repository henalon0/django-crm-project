from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Record

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Username'}),
                               max_length=20)
    
    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Email'}),
                             max_length=50)
    
    password1 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Password'}),
                                max_length=20)
    
    password2 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Confirm Password'}),
                                max_length=20)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RecordForm(forms.ModelForm):
    first_name = forms.CharField(label="",
                                 widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'First Name'}),
                                 max_length=50)
    
    last_name = forms.CharField(label="",
                                widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Last Name'}),
                                max_length=50)
    
    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Email'}),
                             max_length=50)
    
    phone = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Phone'}),
                            max_length=20)
    
    city = forms.CharField(label="",
                           widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'City'}),
                           max_length=50)
    
    state = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'State'}),
                            max_length=50)
    
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'state']


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Email'}),
                             max_length=50)
    
    class Meta:
        fields = ['email']


class PasswordResetForm(UserCreationForm):
    password1 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Password'}),
                                max_length=20)
    
    password2 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': 'mt-4 form-control', 'placeholder': 'Confirm Password'}),
                                max_length=20)
    
    class Meta:
        model = User
        fields = ['password1', 'password2']

        