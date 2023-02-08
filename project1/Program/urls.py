from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('prog', views.prog, name='prog'),
    
    
]