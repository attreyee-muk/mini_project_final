from django.urls import path
from . import views
from django.urls import path,include

urlpatterns = [
    
    path('course_deliverables', views.course_deliverables, name='course_deliverables'),
    
    
]