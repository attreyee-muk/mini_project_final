from django.shortcuts import render,redirect
from Program.models import Program
from accounts.models import User
from timetable.views import final_list

def prog(request):
    user_id=request.user.id
    program_set=Program.objects.all().values()
    
    if request.method=="POST":
        prog_name=request.POST['prog_name']
        prog_id=Program.objects.filter(prog_name=prog_name).values('prog_id')
        final_list['prog_id']=list((prog_id[0]).values())[0]
        
        print(final_list)
        # user_id=request.user.id
        # data=Program.objects.filter(user_id_id=user_id).values()
        # prog_id=request.POST['prog_id']
        # prog_name=request.POST['prog_name']
        # prog_duration=request.POST['prog_duration']
        # prog_desc=request.POST['prog_desc']
        # # tt_id=request.POST['tt_id']
        # user_id=request.user.id
        # en=Program(prog_id=prog_id,prog_name=prog_name,prog_duration=prog_duration,prog_desc=prog_desc,user_id_id=user_id)
        # en.save()
        return redirect('prev')
    
    return render(request,"Program.html",{'program_set':program_set})
# Create your views here.
