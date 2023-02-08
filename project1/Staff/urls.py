from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('staff', views.staff, name='staff'),
    
    
]