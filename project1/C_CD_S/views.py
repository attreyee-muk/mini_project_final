from django.shortcuts import render,redirect
from accounts.models import User

from .models import C_CD_S
# Create your views here.
def c_cd_s(request):
    user_id=request.user.id
    data1=C_CD_S.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=C_CD_S.objects.filter(user_id_id=user_id).values()
        #tt_id=request.POST['tt_id']
        
        course_no_of_units=request.POST['course_no_of_units']
        course_used_no_of_units=request.POST['course_used_no_of_units']
        user_id=request.user.id
        en=C_CD_S(course_no_of_units=course_no_of_units,course_used_no_of_units=course_used_no_of_units,user_id_id=user_id)
        en.save()
        
    return render(request,"C_CD_S.html",{
        'data1':data1,
    })