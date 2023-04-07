from django.shortcuts import render
from .models import Final_data
from timetable.views import final_list
from course.models import Course
from Program.models import Program
from Staff.models import Staff
from Room.models import Room
# from Program_Revision import Program_Revision
from TF_Min.models import TF_Min 
from Class.models import Class
# Create your views here.
def final_data(request):
    user_id=request.user.id
    data2=Final_data.objects.filter(user_id_id=user_id).values()
    tt_id=final_list['tt_id']
    prog_id=final_list['prog_id']
    course_id=final_list['course_id']
    prog_rev_id=final_list['prog_rev_id']
    staff_id=final_list['staff_id']
    room_id=final_list['room_id']
    class_id=final_list['class_id']
    tf_name=final_list['tf_name']
    f_data={
        'course_name':Course.objects.filter(course_id=course_id).values('course_name'),
        'prog_name':Program.objects.filter(prog_id=prog_id).values('prog_name'),
        'staff_name':Staff.objects.filter(staff_id=staff_id).values('staff_name'),
        'room_id':Room.objects.filter(room_id=room_id).values('room_id'),
        'class_name':Class.objects.filter(class_id=class_id).values('class_name')
    }
    l_data=[f_data['course_name'],f_data['prog_name'],f_data['staff_name'],f_data['room_id'],f_data['class_name']]
    return render(request,"Final_data.html")