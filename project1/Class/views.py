from django.shortcuts import render,redirect
from accounts.models import User
from Program_Revision.models import Program_Revision
from Program.models import Program
# #
from Class.models import Class
from Class.models import new_Class_model
from timetable.models import Timetable
from mapping.models import Mapping

def rows_classes(request):
    user_id=request.user.id
    data2=Class.objects.filter(user_id_id=user_id).values()
    classes=[]
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    # data=Mapping.objects.filter(user_id_id=user_id,tt_id=tt_id).values()
    if request.method=="POST":
        row_classes=request.POST.get('rows_classes')
        en2=new_Class_model(no_classes=row_classes,user_id_id=user_id)
        en2.save()
        for i in range(0,int(row_classes)):
            classes.append("0")
        
    return render(request,"Class.html",{'classes':classes,'data2':data2})


def classs(request):
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    user_id=request.user.id
    classes=[]
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
       en1=Class(tt_id=tt_id,class_name=class_name,class_desc=class_desc,class_parent_id=class_parent_id,course_semester=course_semester,user_id_id=user_id)
       en1.save()
       return redirect('room')
       
    return render(request,"Class.html",{'classes':classes,
        'data2':data2
    })

# Create your views here.
