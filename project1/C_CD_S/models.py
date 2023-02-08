from django.db import models

# Create your models here.
from django.db import models

from course.models import Course
from Staff.models import Staff
from course_deliverables.models import Course_Deliverables
from accounts.models import User


class C_CD_S(models.Model):
  c_cd_s_id=models.AutoField(primary_key=True)
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  course_id=models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
  # cd_id=models.IntegerField()#ForeignKey
  cd_id=models.ForeignKey(Course_Deliverables,null=True,on_delete=models.CASCADE)
  staff_id=models.ForeignKey(Staff,null=True,on_delete=models.CASCADE)
  course_no_of_units=models.IntegerField(default=1)
  course_used_no_of_units=models.IntegerField()

