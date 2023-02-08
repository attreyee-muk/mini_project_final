from django.shortcuts import render,redirect

# Create your views here.
from Program_Revision.models import Program_Revision
from Program.models import Program
# #  
from course.models import Course
from accounts.models import User

def cou(request):
    user_id=request.user.id
    data4=Course.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Course.objects.filter(user_id_id=user_id).values()
        course_id=request.POST['course_id']
        #prog_rev_id=request.POST['prog_rev_id']
        #prog_id=request.POST['prog_id']
        course_code=request.POST['course_code']
        course_name=request.POST['course_name']
        course_semester=request.POST['course_semester']
        course_year=request.POST['course_year']
        course_abbr=request.POST['course_abbr']
        #tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Course(course_id=course_id,course_code=course_code,course_name=course_name,course_semester=course_semester,course_year=course_year,course_abbr=course_abbr,user_id_id=user_id)
        en.save()
        return redirect('classs')
    return render(request,"course.html",{
        'data4':data4
    })

