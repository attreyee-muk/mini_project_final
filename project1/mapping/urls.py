from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('mapping1', views.mapping1, name='mapping1'),
    path('generate_timetable', views.generate_timetable, name='generate_timetable'),
]