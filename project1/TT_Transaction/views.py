from django.shortcuts import render,redirect

# Create your views here.
from Class_Schedule.models import Class_Schedule
from C_CD_S.models import C_CD_S
from Room.models import Room
#
from TT_Transaction.models import TT_Transaction
from accounts.models import User

def tt_tra(request):
    user_id=request.user.id
    data14=TT_Transaction.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=TT_Transaction.objects.filter(user_id_id=user_id).values()
        cs_id=request.POST['cs_id']
        c_cd_s_id=request.POST['c_cd_s_id']
        room_id=request.POST['room_id']
        #tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=TT_Transaction(cs_id=cs_id,c_cd_s_id=c_cd_s_id,room_id=room_id,user_id_id=user_id)
        en.save()
        return redirect('')
    return render(request,"",{
        'data14':data14
    })