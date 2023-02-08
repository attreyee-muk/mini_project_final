from django.shortcuts import render,redirect
from Class.models import Class
from Days.models import Days
from Slot.models import Slot
from accounts.models import User
from Class_Schedule.models import Class_Schedule

def Class_Schedule(request):
    user_id=request.user.id
    data3=Class_Schedule.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Class_Schedule.objects.filter(user_id_id=user_id).values()

        cs_id=request.POST['cs_id']
        #class_id=request.POST['class_id']
        #day_id=request.POST['day_id']
        #slot_id=request.POST['slot_id']
        status=request.POST['status']
        #tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Class_Schedule(cs_id=cs_id,status=status,user_id_id=user_id)
        en.save()
    return render(request,"classSchedule.html",{
        'data3':data3
    })

# Create your views here.
