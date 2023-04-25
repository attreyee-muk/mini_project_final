from django.shortcuts import render,redirect
import json
from django.http import JsonResponse
from .models import Mapping
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def generate_timetable():
    print()


def mapping1(request):
    print("done")
    user_id=request.user.id
    data=request.POST.get('data')
    print(type(data))
    data_list=json.loads(data)
    data_list.pop(0)
    print(data_list)
    # try:
    for data in data_list:
            print(data)
            class_data=data['class']
            course_data=data['course']
            room_data=data['room']
            staff_data=data['staff']
            time_data=data['tf']
            mappings=Mapping(user_id_id=user_id,class_data=class_data,course_data=course_data,room_data=room_data,staff_data=staff_data,time_data=time_data)
            print("done")
            mappings.save()
            generate_timetable()
        # response_data={"error":False,"errorMessage":"Updated Successfully"}
        # return redirect('mapping')
    # except:
    #     response_data={"error":True,"errorMessage":"Failed to Update Data"}
    #     return redirect('prog')      
    return render(request,'mappings.html')

