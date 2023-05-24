from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('room', views.room, name='room'),
    path('rows_rooms', views.rows_rooms, name='rows_rooms'),
    
    
]