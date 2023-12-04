# from .models import user
# from django.forms import ModelForm, TextInput
#
#
# class UserForm(ModelForm):
#     class Meta:
#         model = user
#         fields = ['first_name', 'last_name', 'city_id']
#
#         widgets = {
#             'first_name': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'first_name'
#             }),
#
#             'last_name': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'last_name'
#             }),
#
#             'city_id': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'city'
#             })
#         }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, City

class UserRegisterForm(UserCreationForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'city', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

