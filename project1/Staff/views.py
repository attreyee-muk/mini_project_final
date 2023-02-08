from django.shortcuts import render,redirect

# Create your views here.
from Staff.models import Staff
from accounts.models import User

def staff(request):
  user_id=request.user.id
  data12=Staff.objects.filter(user_id_id=user_id).values()
  if request.method=="POST":
      user_id=request.user.id
      data=Staff.objects.filter(user_id_id=user_id).values()
      
      staff_name=request.POST['staff_name']
      staff_abbr=request.POST['staff_abbr']
      staff_status=request.POST['staff_status']
      #tt_id=request.POST['tt_id']
      en=Staff(staff_name=staff_name,staff_abbr=staff_abbr,staff_status=staff_status,user_id_id=user_id)
      en.save()
      
  return render(request,"staff.html",{
        'data12':data12
    })