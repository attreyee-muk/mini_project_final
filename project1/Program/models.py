from django.db import models
from accounts.models import User
# Create your models here.
class Program(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  prog_id=models.AutoField(primary_key=True)
  prog_name=models.CharField(max_length=150)
  prog_duration=models.IntegerField()
  prog_desc=models.CharField(max_length=200)