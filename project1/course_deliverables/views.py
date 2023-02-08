from django.shortcuts import render,redirect
from accounts.models import User

from .models import Course_Deliverables
# Create your views here.

def course_deliverables(request):
    user_id=request.user.id
    data6=Course_Deliverables.objects.filter(user_id_id=user_id).values()
    if request.method=='POST':
        
        cd_name=request.POST['cd_name']
        cd_desc=request.POST['cd_desc']
        cd_duration_min=request.POST['cd_duration_min']
        # tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Course_Deliverables(cd_name=cd_name,cd_desc=cd_desc,cd_duration_min=cd_duration_min,user_id_id=user_id)
        en.save()

        # data=Course_Deliverables.objects.filter(user_id_id=user_id).values()
        # print(" ",data)
        
    return render(request,'course_deliverables.html',{
        'data6':data6,
    })
