from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    path('university', views.university, name='university'),
]