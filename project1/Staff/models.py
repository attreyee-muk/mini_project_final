from django.db import models
from accounts.models import User

class Staff(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  staff_id=models.AutoField(primary_key=True)
  staff_name=models.CharField(max_length=50)
  staff_abbr=models.CharField(max_length=100)
  staff_status=models.BooleanField()
# Create your models here.
