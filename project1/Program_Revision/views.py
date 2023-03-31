from django.shortcuts import render,redirect
from Program.models import Program
from Program_Revision.models import Program_Revision
from accounts.models import User
from timetable.views import final_list


def prev(request):
    user_id=request.user.id
    data9=Program_Revision.objects.all().values()
    if request.method=="POST":
        prog_rev_name=request.POST['prog_rev_name']
        prog_rev_id=Program_Revision.objects.filter(prog_rev_name=prog_rev_name).values('prog_rev_id')
        final_list['prog_rev_id']=list((prog_rev_id[0]).values())[0]
        # user_id=request.user.id
        # data=Program_Revision.objects.filter(user_id_id=user_id).values()
        # prog_rev_id=request.POST['prog_rev_id']
        # prog_rev_start_dt=request.POST['prog_rev_start_dt']
        # prog_rev_end_dt=request.POST['prog_rev_end_dt']
        # # prog_id=request.POST['prog_id']
        # prog_rev_name=request.POST['prog_rev_name']
        # prog_rev_desc=request.POST['prog_rev_desc']
        # prog_rev_status=request.POST['prog_rev_status']
        # # tt_id=request.POST['tt_id']
        # user_id=request.user.id
        # en=Program_Revision(prog_rev_id=prog_rev_id,prog_rev_start_dt=prog_rev_start_dt,prog_rev_end_dt=prog_rev_end_dt,prog_rev_name=prog_rev_name,prog_rev_desc=prog_rev_desc,prog_rev_status=prog_rev_status,user_id_id=user_id)
        # en.save()
        return redirect('cou')
    return render(request,"Program_revision.html",{
        'data9':data9
    })

# Create your views here.
