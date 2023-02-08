from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('c_cd_s', views.c_cd_s, name='c_cd_s'),
    
    
]