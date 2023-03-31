from django.db import models
from accounts.models import User
from university.models import University
# Create your models here.
class Program(models.Model):
  
  prog_id=models.IntegerField()
  
  prog_name=models.CharField(max_length=150)
  prog_duration=models.IntegerField()
  prog_desc=models.CharField(max_length=2000)
  university=models.ForeignKey(University,null=True,on_delete=models.CASCADE)


  
  # class Meta:
  #   unique_together=(("user_id","prog_id"),)