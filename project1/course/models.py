

# Create your models here.
from django.db import models
from Program_Revision.models import Program_Revision
from Program.models import Program
from accounts.models import User
from university.models import University
# Create your models here.
class Course(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  course_id=models.AutoField(primary_key=True)
  prog_rev_id=models.IntegerField()#ForeignKey
  # prog_rev_id=models.ForeignKey(Program_Revision,null=True,on_delete=models.CASCADE)
  #prog_id=models.IntegerField()#ForeignKey
  prog_id=models.ForeignKey(Program,null=True,on_delete=models.CASCADE)
  course_code=models.CharField(max_length=40)
  course_name=models.CharField(max_length=100)
  course_semester=models.CharField(max_length=100)
  course_year=models.CharField(max_length=100)
  course_abbr=models.CharField(max_length=100)
  university=models.ForeignKey(University,null=True,on_delete=models.CASCADE)
  
