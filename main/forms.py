from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, City
from django.contrib.auth import get_user_model
from django.forms.widgets import PasswordInput, TextInput
User = get_user_model()
class UserRegisterForm(UserCreationForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, empty_label="Select a city")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'city')

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

