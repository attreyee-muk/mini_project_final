from django.shortcuts import render,redirect
from course.models import Course
from course_deliverables.models import Course_Deliverables
from Course_Del_Units.models import Course_Del_Units
from accounts.models import User

def cdu(request):
    user_id=request.user.id
    data5=Course_Del_Units.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Course_Del_Units.objects.filter(user_id_id=user_id).values()
        del_units=request.POST['del_units']
        user_id=request.user.id
        en=Course_Del_Units(del_units=del_units,user_id_id=user_id)
        en.save()
        
        
    return render(request,"Course_Del_Units.html",{
        'data5':data5
    })
# Create your views here.
