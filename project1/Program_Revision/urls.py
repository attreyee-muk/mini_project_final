from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('prev', views.prev, name='prev'),
    
    
]