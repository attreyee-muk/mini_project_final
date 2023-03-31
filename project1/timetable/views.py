from django.shortcuts import render,redirect
from .models import Timetable

# Create your views here.
final_list={'tt_id':0,'prog_id':0,'prog_rev_id':0,'course_id':0}
print(final_list)

def time_table(request):
    user_id=request.user.id
    data2=Timetable.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
       tt_id=request.POST['tt_id']
       final_list['tt_id']=tt_id
       tt_name=request.POST['tt_name']
       tt_desc=request.POST['tt_desc']
       start_date=request.POST['start_date']
       end_date=request.POST['end_date']
       user_id=request.user.id
       en1=Timetable(tt_id=tt_id,tt_name=tt_name,tt_desc=tt_desc,start_date=start_date,end_date=end_date,user_id_id=user_id)
       en1.save()
       print(final_list)
       return redirect('prog')
       
    return render(request,"timetable.html",{
        'data2':data2
    })