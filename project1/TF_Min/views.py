from django.shortcuts import render,redirect
from TF_Min.models import TF_Min
from accounts.models import User

def tfmin(request):
    user_id=request.user.id
    data13=TF_Min.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
        # user_id=request.user.id
        # data=TF_Min.objects.filter(user_id_id=user_id).values()
        
        tf_name=request.POST['tf_name']
        tf_minutes=request.POST['tf_minutes']
        user_id=request.user.id
        en=TF_Min(tf_name=tf_name,tf_minutes=tf_minutes,user_id_id=user_id)
        en.save()
        
    return render(request,"TF_Min.html",{
        'data13':data13
    })
# Create your views here.
