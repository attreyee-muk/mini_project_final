from django.db import models
from django.contrib.auth.models import User
from Program.models import Program
from university.models import University
from course.models import Course
from timetable.models import Timetable
from TF_Min.models import TF_Min
from Program_Revision.models import Program_Revision
from timetable.models import Timetable
# Create your models here.
# class Institutions(models.Model):
#     inst_id=models.AutoField(primary_key=True)
#     inst_name = models.CharField(max_length=100)
#     inst_admin_name = models.CharField(max_length=100)
#     inst_email = models.EmailField()
#     inst_admin_email = models.EmailField()  
#     inst_contact = models.CharField(max_length=100)
#     inst_admin_contact = models.CharField(max_length=100)
#     inst_address = models.CharField(max_length=100)
#     passwd = models.CharField(max_length=100)

class user_roles(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=100)



