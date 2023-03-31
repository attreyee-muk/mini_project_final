from django.shortcuts import render
from .models import Final_data
from timetable.views import final_list
from course.models import Course
# Create your views here.
def final_data(request):
    user_id=request.user.id
    data2=Final_data.objects.filter(user_id_id=user_id).values()
    tt_id=final_list['tt_id']
    prog_id=final_list['prog_id']
    course_id=final_list['course_id']
    prog_rev_id=final_list['prog_rev_id']
    return render(request,"Final_data.html")