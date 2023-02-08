from django.http import HttpResponse
from django.shortcuts import redirect 

def unautheticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin_dashboard') #to be changed to homee
        else:
            return view_func(request, *args, **kwargs)
        return view_func(request,*args, **kwargs)
    return wrapper_func