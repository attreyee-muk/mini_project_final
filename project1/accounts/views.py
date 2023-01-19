# Create your views here.
import email
from django.forms import PasswordInput
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Institutions
from . import models
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
import hashlib 

# Create your views here.
def home(request):
    if 'inst_id' in request.session:
        current_user = request.session['inst_id']
        param = {'inst_id': current_user}
        return render(request, 'index.html', param)
    else:
        return redirect('login')
    #return render(request, 'choose.html') #why? 

def register(request):
    if request.method=="POST":
        inst_name = request.POST['inst_name']
        inst_admin_name = request.POST['inst_admin_name']
        inst_email = request.POST['inst_email']
        inst_admin_email = request.POST['inst_admin_email']
        inst_contact = request.POST['inst_contact']
        inst_admin_contact = request.POST['inst_admin_contact']
        inst_address = request.POST['inst_address']
        passwd = request.POST['passwd']
        confirm_passwd = request.POST['confirm_passwd']

        en=Institutions(inst_name = inst_name, inst_admin_name = inst_admin_name, inst_email = inst_email, inst_admin_email = inst_admin_email, inst_contact = inst_contact, inst_admin_contact = inst_admin_contact, inst_address = inst_address, passwd = str(hashlib.md5(passwd.encode()).hexdigest()))
        if passwd==confirm_passwd:
           en.save()
           return redirect('login')
           print("valid")
        else:
            print("Invalid Password")
        print("data has been written")
    return render(request,"pages/examples/register.html")



def handlelogin(request):
    if request.method=='POST':
        inst_email=request.POST['inst_email']
        passwd=str(hashlib.md5(request.POST['passwd'].encode()).hexdigest())
        data=models.Institutions.objects.filter(inst_email=inst_email,passwd=passwd).values()
        print(data)
        if data:
            request.session['inst_id'] = data[0]['inst_id']
            inst_id = request.session['inst_id']
            param = {'inst_id': inst_id}
            return render(request, 'index.html', param)
        else:
            return redirect('register')

    return render(request, 'pages/examples/login.html')
 
def admin_dashboard(request):
    return render(request,'index.html')


def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request,"choose.html")

@login_required(login_url='login.html')
def adminpaged(request):
    return render(request,'adminpaged.html')