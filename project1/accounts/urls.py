from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.handlelogin, name='login'),
    path('register', views.register, name='register'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
]
