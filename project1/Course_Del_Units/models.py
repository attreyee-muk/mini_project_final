# Create your models here.
from django.db import models
from course.models import Course
from course_deliverables.models import Course_Deliverables
from accounts.models import User
# Create your models here.


class Course_Del_Units(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  course_id=models.ForeignKey(Course,null=True,on_delete=models.CASCADE)   
  
  # cd_id=models.ForeignKey(Course_Deliverables,null=True,on_delete=models.CASCADE)
  del_units=models.IntegerField()
