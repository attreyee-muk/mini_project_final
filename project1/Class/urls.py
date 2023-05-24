from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('classs', views.classs, name='classs'),
    path('rows_classes', views.rows_classes, name='rows_classes'),
]