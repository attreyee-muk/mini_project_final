from django.shortcuts import render,redirect
from Program.models import Program
from accounts.models import User

def prog(request):
    user_id=request.user.id
    data8=Program.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=Program.objects.filter(user_id_id=user_id).values()
        prog_id=request.POST['prog_id']
        prog_name=request.POST['prog_name']
        prog_duration=request.POST['prog_duration']
        prog_desc=request.POST['prog_desc']
        # tt_id=request.POST['tt_id']
        user_id=request.user.id
        en=Program(prog_id=prog_id,prog_name=prog_name,prog_duration=prog_duration,prog_desc=prog_desc,user_id_id=user_id)
        en.save()
        return redirect('prev')
    return render(request,"Program.html",{
        'data8':data8
    })
# Create your views here.
