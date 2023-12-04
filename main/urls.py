# from django.urls import path
# from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('home', views.home, name='home'),
    path('profile/', views.profile, name='profile')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)