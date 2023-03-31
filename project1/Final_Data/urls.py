from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [ 
    path('final_data', views.final_data, name='final_data'),
]