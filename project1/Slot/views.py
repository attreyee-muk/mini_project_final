from django.shortcuts import render,redirect
from Slot.models import Slot
from accounts.models import User

def slot(request):
    user_id=request.user.id
    data11=Slot.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Slot.objects.filter(user_id_id=user_id).values()
        slot_id=request.POST['slot_id']
        slot_desc=request.POST['slot_desc']
        slot_start_time=request.POST['slot_start_time']
        slot_end_time=request.POST['slot_end_time']
        slot_status=request.POST['slot_status']
        #tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Slot(slot_id=slot_id,slot_desc=slot_desc,slot_start_time=slot_start_time,slot_end_time=slot_end_time,slot_status=slot_status,user_id_id=user_id)
        en.save()
        
    return render(request,"slot.html",{
        'data11':data11
    })
# Create your views here.
