from django.db import models

# Create your models here.
from django.db import models
from Program_Revision.models import Program_Revision
from Program.models import Program
from Program_Revision.models import Program_Revision
from accounts.models import User
# Create your models here.

class Class(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  class_id=models.AutoField(primary_key=True)
  class_name=models.CharField(max_length=100)
  class_desc=models.CharField(max_length=100)
  class_parent_id=models.IntegerField()
  prog_rev_id=models.IntegerField()#ForeignKey
  prog_rev_id=models.ForeignKey(Program_Revision,null=True,on_delete=models.CASCADE)
  prog_id=models.IntegerField()#ForeignKey
  prog_id=models.ForeignKey(Program,null=True,on_delete=models.CASCADE)
  course_semester=models.IntegerField()

