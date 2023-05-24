from django.shortcuts import render,redirect

# Create your views here.
from Staff.models import Staff
from accounts.models import User
from timetable.models import Timetable
def rows_staff(request):
    user_id=request.user.id
    data12=Staff.objects.filter(user_id_id=user_id).values()
    staff=[]
    if request.method=="POST":
        rows_staff=request.POST.get('rows_staff')
        
        for i in range(0,int(rows_staff)):
            staff.append("0")
        
    return render(request,"Staff.html",{'staff':staff,'data12':data12})

def staff(request):
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    user_id=request.user.id
    staff=[]
    data12=Staff.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
      user_id=request.user.id
      data12=Staff.objects.filter(user_id_id=user_id).values()
      
      staff_name=request.POST['staff_name']
      staff_abbr=request.POST['staff_abbr']
      staff_status=request.POST['staff_status']
      #tt_id=request.POST['tt_id']
      en=Staff(tt_id=tt_id,staff_name=staff_name,staff_abbr=staff_abbr,staff_status=staff_status,user_id_id=user_id)
      en.save()
      return redirect('DCapp')
      
    return render(request,"Staff.html",{'staff':staff,'data12':data12})