from django.shortcuts import render,redirect
from Room.models import Room
from accounts.models import User
from timetable.models import Timetable

def rows_rooms(request):
    user_id=request.user.id
    data10=Room.objects.filter(user_id_id=user_id).values()
    rooms=[]
    if request.method=="POST":
        rows_courses=request.POST.get('rows_rooms')
        
        for i in range(0,int(rows_courses)):
            rooms.append("0")
        
    return render(request,"Room.html",{'rooms':rooms,'data10':data10})
def room(request):
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    user_id=request.user.id
    rooms=[]
    data10=Room.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Room.objects.filter(user_id_id=user_id).values()
        room_number=request.POST['room_number']
        room_desc=request.POST['room_desc']
        room_label_abbr=request.POST['room_label_abbr']
        room_seating_cap=request.POST['room_seating_cap']
        room_type=request.POST['room_type']
        #tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Room(tt_id=tt_id,room_number=room_number,room_desc=room_desc,room_label_abbr=room_label_abbr,room_seating_cap=room_seating_cap,room_type=room_type,user_id_id=user_id)
        en.save()
        return redirect('staff')
        
    return render(request,"Room.html",{
        'data10':data10,'rooms':rooms
    })
# Create your views here.
