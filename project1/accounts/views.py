# # Create your views here.
# import email
# from django.forms import PasswordInput
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from accounts.models import Institutions
from . models import user_roles
from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password
# import hashlib 
from university.models import University
from . decorators import unautheticated_user
# Create your views here.

user_id=1
def home(request):
    return render(request,"index.html")

def final(request):
  return render(request,'Final_data.html')

@login_required(login_url='login')
def admin_dashboard(request):
    user_id=request.user.id
    data_uni_name=University.objects.values_list('uni_name')
    print(data_uni_name)
    return render(request,"admin_dashboard.html",{
        'data_uni_name':data_uni_name,
    })

@unautheticated_user
def handlelogin(request):
    global user_id
    if request.method=="POST":
      username=request.POST['username']
      password = request.POST['password']
      user=authenticate(request, username=username,password=password)
      
      if user is not None:
        login(request,user)
        user_info=User.objects.filter(username=username).values()
        
        user_id=user_info[0].get('id')

        user_details=user_roles.objects.filter(user_id_id=user_id).values()
        print(user_details)
        user_role=user_details[0].get('role')
        
        print("valid")
        if(user_role=='Student'):
            return redirect('student_dashboard')
        elif (user_role=='Admin'):
            return redirect('admin_dashboard')
        else:
            return redirect('staff_dashboard')
        #Home Page
      else:
        print("invalid")
        #  messages.info(request,"Invalid Credentials")
        return redirect('login')
    else:
      return render(request,"pages/examples/login.html")

@login_required(login_url='login')
def logout(request):
   auth.logout(request) 
   return redirect("/")



@unautheticated_user
def register(request):
    global user_id
    if request.method=="POST":
       first_name=request.POST.get('first_name')
       last_name=request.POST['last_name']
       username=request.POST['username']
       email=request.POST['email']
       role=request.POST['role']
       password = request.POST['password']
       password2 = request.POST['password2']
       if password==password2:
            if User.objects.filter(username=username).exists():
               print("Username taken")
            else:
               user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
               user.save()
               
               user_info=user_roles.objects.create(user_id=User.objects.latest('id'), role=role)
               user_info.save()

               print("User Created")
               if(role=='Admin'):
                return redirect('admin_dashboard')
               elif (role=='Student'):
                return redirect('login')
               else :
                return redirect('register')
            return redirect('register')
    # if role=="Admin":
    #     return render(request,"templates/index.html") 
    #     or redirect('admin_dashboard')
    # elif role=="Teacher":
    #     return render(request,"")
    # else:
    #     return render(request,"")

    return render(request,"pages/examples/register.html")
def student_dashboard(request):
  return render(request,'student_dashboard.html')
def staff_dashboard(request):
  return render(request,'staff_dashboard.html')


print(user_id)