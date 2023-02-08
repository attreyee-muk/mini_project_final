from django.shortcuts import render,redirect
from Days.models import Days
from accounts.models import User

def days(request):
    user_id=request.user.id
    data7=Days.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Days.objects.filter(user_id_id=user_id).values()
        day_id=request.POST['day_id']
        day_name=request.POST['day_name']
        day_abbr=request.POST['day_abbr']
        day_order=request.POST['day_order']
        day_status=request.POST['day_status']
        # tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Days(day_id=day_id,day_name=day_name,day_abbr=day_abbr,day_order=day_order,day_status=day_status,user_id_id=user_id)
        en.save()
        return redirect ('room')
    return render(request,"Days.html",{
        'data7':data7
    })

# Create your views here.
