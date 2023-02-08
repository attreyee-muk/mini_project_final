from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('tt_tra', views.tt_tra, name='tt_tra'),
    
    
]