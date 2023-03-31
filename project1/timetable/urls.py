from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    path('time_table', views.time_table, name='time_table'),
]