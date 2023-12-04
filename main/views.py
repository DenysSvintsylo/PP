# from django.shortcuts import render, redirect
# from .forms import UserForm
#
#
# def register(request):
#     error = ''
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#
#             error = 'incorrect form'
#
#     form = UserForm()
#     data = {
#         'form': form,
#         'eror': error
#     }
#     return render(request, 'main/register.html', data)
#
# def home(request):
#     return render(request, 'main/home.html')
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser, City, Mall

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
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

