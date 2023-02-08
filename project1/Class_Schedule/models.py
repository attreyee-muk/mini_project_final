# Create your models here.
from django.db import models
from Class.models import Class
from Days.models import Days
from Slot.models import Slot
from accounts.models import User

class Class_Schedule(models.Model):
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  cs_id=models.AutoField(primary_key=True)
  # class_id=models.IntegerField()#ForeignKey
  class_id=models.ForeignKey(Class,models.DO_NOTHING,db_column='class_id')
  # day_id=models.IntegerField()#ForeignKey
  day_id=models.ForeignKey(Days,models.DO_NOTHING,db_column='day_id')
  # slot_id=models.IntegerField()#ForeignKey
  slot_id=models.ForeignKey(Slot,models.DO_NOTHING,db_column='slot_id')
  status=models.CharField(max_length=50)
