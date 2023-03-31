from django.urls import path
from . import views
from django.urls import path,include
urlpatterns = [
    
    path('', views.home, name='home'),
    path('login', views.handlelogin, name='login'),
    path('register', views.register, name='register'),
    path('logout',views.logout,name='logout'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('staff_dashboard', views.staff_dashboard, name='staff_dashboard'),
    path('final', views.final, name='final'),
    path('',include('course_deliverables.urls')),
    path('',include('C_CD_S.urls')),
    path('',include('Class.urls')),
    path('',include('Class_Course.urls')),
    path('',include('Class_Schedule.urls')),
    path('',include('course.urls')),
    path('',include('Course_Del_Units.urls')),
    path('',include('Days.urls')),
    path('',include('Program.urls')),
    path('',include('Program_Revision.urls')),
    path('',include('Room.urls')),
    path('',include('Slot.urls')),
    path('',include('Staff.urls')),
    path('',include('TF_Min.urls')),
    path('',include('TT_Transaction.urls')),
    path('',include('university.urls')),
    path('',include('timetable.urls')),
    path('',include('Final_Data.urls')),
]
