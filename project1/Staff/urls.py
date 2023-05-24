from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('staff', views.staff, name='staff'),
    path('rows_staff', views.rows_staff, name='rows_staff'),
]