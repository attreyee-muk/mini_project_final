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

class initial_data(models.Model):
  initial_data_id=models.AutoField(primary_key=True)
  user_id=models.ForeignKey(User , on_delete=models.CASCADE)
  tt_name=models.CharField(max_length=150)
  prog_name=models.CharField(max_length=150)

  
 