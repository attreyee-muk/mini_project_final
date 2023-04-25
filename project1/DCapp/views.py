from django.shortcuts import render
from accounts.models import User
from DCapp.models import input_values

# Create your views here.
def DCapp(request):
    user_id=request.user.id
    if request.method=="POST":
        no_days=request.POST['no_days']
        no_classes=request.POST['no_classes']
        en1=input_values(no_classes=no_classes,no_days=no_days)
        en1.save()
    return render(request,'DCapp.html')