from django.db import models
from accounts.models import User
from Program.models import Program
# Create your models here.
class Program_Revision(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  prog_rev_id=models.AutoField(primary_key=True)
  prog_rev_start_dt=models.DateField()
  prog_rev_end_dt=models.DateField()
  prog_id=models.ForeignKey(Program,null=True,on_delete=models.CASCADE)
  prog_rev_name=models.CharField(max_length=300)
  prog_rev_desc=models.CharField(max_length=300)
  prog_rev_status=models.BooleanField()