from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser, City, Mall
from rest_framework import generics
from .serializers import MallSerializer


class MallList(generics.ListAPIView):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer

class MallDetail(generics.RetrieveAPIView):
    queryset = Mall.objects.all()
    serializer_class = MallSerializer


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})

def home(request):
    # Fetch malls based on user's city
    user_city = request.user.city
    malls = Mall.objects.filter(city=user_city) if user_city else []
    return render(request, 'main/home.html', {'malls': malls})

def profile(request):
    return render(request, 'main/profile.html')

