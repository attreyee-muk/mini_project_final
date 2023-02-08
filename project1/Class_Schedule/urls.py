from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('Class_Schedule', views.Class_Schedule, name='Class_Schedule'),
    
    
]