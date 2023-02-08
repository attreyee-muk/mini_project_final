from django.db import models

# Create your models here.
from django.db import models
from Class.models import Class
# from course.models import Course
# #
from accounts.models import User

# Create your models here.
class Class_Course(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  class_id=models.AutoField(primary_key=True)#ForeignKey
  class_id=models.ForeignKey(Class,models.DO_NOTHING,db_column='class_id')
  course_id=models.IntegerField()#ForeignKey

