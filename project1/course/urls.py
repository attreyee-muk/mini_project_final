from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('cou', views.cou, name='cou'),
    path('cou_rows_courses', views.cou_rows_courses, name='cou_rows_courses'),
    
]