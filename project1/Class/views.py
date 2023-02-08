from django.shortcuts import render,redirect
from accounts.models import User
from Program_Revision.models import Program_Revision
from Program.models import Program
# #
from Class.models import Class
def classs(request):
    user_id=request.user.id
    data2=Class.objects.filter(user_id_id=user_id).values()
    if request.method=="POST":
    #    user_id=request.user.id
    #    data=Class.objects.filter(user_id_id=user_id).values()  
       
       class_name=request.POST['class_name']
       class_desc=request.POST['class_desc']
       class_parent_id=request.POST['class_parent_id']
      # prog_rev_id=request.POST['prog_rev_id']
      # prog_id=request.POST['prog_id']
       course_semester=request.POST['course_semester']
      # tt_id=request.POST['tt_id']
       user_id=request.user.id
       en1=Class(class_name=class_name,class_desc=class_desc,class_parent_id=class_parent_id,course_semester=course_semester,user_id_id=user_id)
       en1.save()
       
    return render(request,"Class.html",{
        'data2':data2
    })

# Create your views here.
