from django.shortcuts import render,redirect

# Create your views here.
from Program_Revision.models import Program_Revision
from Program.models import Program
# #  
from course.models import Course
from accounts.models import User
from timetable.views import final_list
from django.http import JsonResponse

def cou(request):
    user_id=request.user.id
    courses=Course.objects.values('course_name')
    return JsonResponse({'courses':list(courses.values())})
    
    if request.method=="POST":
        # user_id=request.user.id
        # data=Course.objects.filter(user_id_id=user_id).values()
        # course_id=request.POST['course_id']
        # #prog_rev_id=request.POST['prog_rev_id']
        # #prog_id=request.POST['prog_id']
        # course_code=request.POST['course_code']
        course_name=request.POST['course_name']
        course_id=Course.objects.filter(course_name=course_name).values('course_id')
        final_list['course_id']=list((course_id[0]).values())[0]
        print(final_list)
        # course_semester=request.POST['course_semester']
        # course_year=request.POST['course_year']
        # course_abbr=request.POST['course_abbr']
        # #tt_id=request.POST['tt_id']
        # user_id=request.user.id
        # en=Course(course_id=course_id,course_code=course_code,course_name=course_name,course_semester=course_semester,course_year=course_year,course_abbr=course_abbr,user_id_id=user_id)
        # en.save()
        return redirect('final_data')
    return render(request,"mapping.html",{'data4':data4})


#Back to being single. I am not worthy of a relationship. You will be forever alone. You can never make anyone happy. Sadness is what you will give coz you are a sadist. 
