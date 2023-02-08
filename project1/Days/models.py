from django.db import models
from accounts.models import User
# Create your models here.
class Days(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  day_id=models.AutoField(primary_key=True)
  day_name=models.CharField(max_length=10)
  day_abbr=models.CharField(max_length=10)
  day_order=models.IntegerField()
  day_status=models.BooleanField()