from django.shortcuts import render,redirect
from .models import University
# Create your views here.
def university(request):
    user_id=request.user.id
    data_uni_name=University.objects.values_list('uni_name')
    print(data_uni_name)
    if request.method=='POST':
        uni_name=request.POST['uni_name']
        user_id=request.user.id
        return redirect('time_table')
    return render(request,'admin_dashboard.html',{
        'data_uni_name':data_uni_name,
    })