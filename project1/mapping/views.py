from django.shortcuts import render,redirect
import json
from django.http import JsonResponse
from .models import Mapping
from django.views.decorators.csrf import csrf_protect
from Program.models import Program
from Class.models import Class
from Class.models import new_Class_model
from timetable.models import Timetable
from course.models import Course
from course.models import new_Course_model
from Staff.models import Staff
from Room.models import Room
from accounts.models import User
from DCapp.models import input_values
import random
# Create your views here.


tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
no_course=new_Course_model.objects.latest('user_id_id','tt_id').no_courses
no_classes=new_Class_model.objects.latest('user_id_id','tt_id').no_classes
no_periods=input_values.objects.latest('user_id_id','tt_id').no_periods
no_days=input_values.objects.latest('user_id_id','tt_id').no_days
data=Mapping.objects.values('class_data').distinct()


def generate_timetable(request):
    global user_id
    user_id=request.user.id
    
    print(data)
    return render(request,'generate_timetable.html',{'sec_data':sec_data})


def mapping1(request):
    tt_id1=Timetable.objects.latest()
    tt_id=tt_id1.tt_id
    # no_course=new_Course_model.objects.latest('user_id_id').no_courses
    # no_classes=new_Class_model.objects.latest('user_id_id').no_classes
    # print(no_course,no_classes)

    user_id=request.user.id
    tt_id=Timetable.objects.latest('user_id_id','tt_id').tt_id
    data=Mapping.objects.filter(tt_id=tt_id).values()
    global courses
    courses=Course.objects.filter(user_id_id=user_id,tt_id=tt_id).values()
    print(data)
    global classes
    classes=Class.objects.filter(user_id_id=user_id,tt_id=tt_id).values()
    global rooms
    rooms=Room.objects.filter(user_id_id=user_id,tt_id=tt_id).values()
    global staff
    staff=Staff.objects.filter(user_id_id=user_id,tt_id=tt_id).values()
    if(request.method=="POST"):
        class_data=request.POST['class_data']
        course_data=request.POST['course_data']
        room_data=request.POST['room_data']
        staff_data=request.POST['staff_data']
        time_data=request.POST['time_data']
        en=Mapping(class_data=class_data,course_data=course_data,room_data=room_data,staff_data=staff_data,time_data=time_data,user_id_id=user_id,tt_id=tt_id)
        en.save()

       
    return render(request,'mappings.html',{'courses':courses,'classes':classes, 'rooms':rooms, 'staff':staff,'data':data})



#Timetable generation 
arr_days=[]
periods_plus_days=[]
sections=[[[0, 0,0,0,0], [0, 0,0,0,0],[0, 0,0,0,0],[0, 0,0,0,0],[0, 0,0,0,0]], [[0, 0,0,0,0], [0, 0,0,0,0],[0, 0,0,0,0],[0, 0,0,0,0],[0, 0,0,0,0]]]
for i in range(no_days):
    arr_days.append(0)
for i in range(no_periods):
    periods_plus_days.append(arr_days)

for i in range(2):
    sections.append(periods_plus_days)
each_section=[]
all_classes=[]

for i in range(2):
    each_section.append(data[i]['class_data'])


for j in each_section:
    all_classes.append(Mapping.objects.filter(class_data=j).values())

print(sections)
print(all_classes[0][2])
comparisons=0
hashmaps={0:0,1:0,2:0,3:0,4:0}

def random_generation():
    
    index=random.randint(0,4)
    hashmaps[index]=hashmaps[index]+1
    while(hashmaps[index]>2):
        hashmaps[index]=hashmaps[index]-1
        index=random.randint(0,4)
        hashmaps[index]+=1
    print(index," ",hashmaps)
    return index



for classes in range(0,2):
    for row in range(0,no_days):
        for column in range(0,no_periods):
            if((classes==0)):
                index=random_generation()
                sections[classes][row][column]=all_classes[0][index]
            else:
                i=0
                index=random_generation()
                sections[classes][row][column]=all_classes[classes][index]
                while ((i<comparisons) and sections[classes][row][column]['staff_data']==sections[classes-1][row][column]['staff_data']):
                    index=random_generation()
                    sections[classes][row][column]=all_classes[classes][index]
                    i=i+1
        hashmaps={0:0,1:0,2:0,3:0,4:0}

    hashmaps={0:0,1:0,2:0,3:0,4:0}
    comparisons+=1

sec_data=[]          
for i in range (len(sections)-2):
    print(sections[i])
    sec_data.append(sections[i])
    print("\n")

print(len(sec_data))




# for i in range(0,5):
#     random_generation()

