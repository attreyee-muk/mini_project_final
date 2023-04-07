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
class Final_data(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    prog_id=models.ForeignKey(Program, on_delete=models.CASCADE)
    uni_id=models.ForeignKey(University, on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    tt_id=models.ForeignKey(Timetable, on_delete=models.CASCADE)

