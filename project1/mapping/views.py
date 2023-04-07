from django.shortcuts import render,redirect
import json
from django.http import JsonResponse
from .models import Mapping
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def mapping(request):
    print("done")
    user_id=request.user.id
    data=request.POST.get("data")
    print(type(data))
    data_list=json.loads(data)
    
    try:
        for data in data_list:
            mappings=Mapping()
            map=[]
            Mapping.user_id_id=user_id
            Mapping.class_data=data['class']
            Mapping.course_data=data['course']
            Mapping.room_data=data['room']
            Mapping.staff_data=data['staff']
            Mapping.time_data=data['tf']
            print("done")
            mappings.save()
        response_data={"error":False,"errorMessage":"Updated Successfully"}
        return redirect('mapping')
    except:
        response_data={"error":True,"errorMessage":"Failed to Update Data"}
        return redirect('prog')
    
    return render(request,'mappings.html')

