from django.shortcuts import render,redirect
from Room.models import Room
from accounts.models import User

def room(request):
    user_id=request.user.id
    data10=Room.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Room.objects.filter(user_id_id=user_id).values()
        room_id=request.POST['room_id']
        room_desc=request.POST['room_desc']
        room_label_abbr=request.POST['room_label_abbr']
        room_seating_cap=request.POST['room_seating_cap']
        room_type=request.POST['room_type']
        #tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Room(room_id=room_id,room_desc=room_desc,room_label_abbr=room_label_abbr,room_seating_cap=room_seating_cap,room_type=room_type,user_id_id=user_id)
        en.save()
        
    return render(request,"rooms.html",{
        'data10':data10
    })
# Create your views here.
