from django.db import models
from accounts.models import User
# Create your models here.
class Slot(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  slot_id=models.AutoField(primary_key=True)
  slot_desc=models.CharField(max_length=150)
  slot_start_time=models.TimeField()
  slot_end_time=models.TimeField()
  slot_status=models.BooleanField()