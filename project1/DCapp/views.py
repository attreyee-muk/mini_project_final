from django.shortcuts import render,redirect
from accounts.models import User
from DCapp.models import input_values
from mapping.models import Mapping
from timetable.models import Timetable
# Create your views here.
def DCapp(request):
    user_id=request.user.id
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    data=Mapping.objects.filter(user_id_id=user_id,tt_id=tt_id).values()
    if request.method=="POST":
        no_days=request.POST['no_days']
        no_periods=request.POST['no_periods']
        en1=input_values(no_periods=no_periods,no_days=no_days,user_id_id=user_id)
        en1.save()
        return redirect('mapping1')
    return render(request,'DCapp.html')