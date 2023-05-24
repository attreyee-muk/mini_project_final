from django.shortcuts import render,redirect

# Create your views here.
from Program_Revision.models import Program_Revision
from Program.models import Program
from Program.views import final_list
from course.models import new_Course
from course.models import Course
from course.models import new_Course_model
from accounts.models import User
from timetable.views import final_list
from django.http import JsonResponse
from timetable.models import Timetable
from mapping.models import Mapping

def cou_rows_courses(request):
    user_id=request.user.id
    data4=Course.objects.filter(user_id_id=user_id).values()
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    # data=Mapping.objects.filter(user_id_id=user_id,tt_id=tt_id).values()
    courses=[]
    if request.method=="POST":
        rows_courses=request.POST.get('rows_courses')
        en1=new_Course_model(no_courses=rows_courses,user_id_id=user_id)
        en1.save()
        for i in range(0,int(rows_courses)):
            courses.append("0")
        
    return render(request,"course.html",{'courses':courses,'data4':data4})


def cou(request):
    user_id=request.user.id
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    global courses
    courses=[]
    global data4
    data4=Course.objects.filter(user_id_id=user_id).values()
    
    if request.method=="POST":
        user_id=request.user.id
        prog_id=final_list['prog_id']
        university_id=1
        prog_rev_id=1
        course_code=request.POST['course_code']
        course_name=request.POST['course_name']
        
        # final_list['course_id']=list((course_id[0]).values())[0]
        # print(final_list)
        course_semester=request.POST['course_semester']
        course_year=request.POST['course_year']
        course_abbr=request.POST['course_abbr']
        #tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Course(tt_id=tt_id,course_code=course_code,course_name=course_name,course_semester=course_semester,course_year=course_year,course_abbr=course_abbr,user_id_id=user_id,university_id=university_id,prog_rev_id=prog_rev_id)
        en.save()
        
        return redirect('classs')

        # return redirect('cou')
    return render(request,"course.html",{'courses':courses,'data4':data4})




