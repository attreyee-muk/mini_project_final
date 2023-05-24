from django.db import models
from accounts.models import User
# Create your models here.
class Room(models.Model):
  tt_id=models.IntegerField()
  user_id=models.ForeignKey(User, on_delete=models.CASCADE)
  room_id=models.AutoField(primary_key=True)
  room_desc=models.CharField(max_length=120)
  room_label_abbr=models.CharField(max_length=130)
  room_seating_cap=models.IntegerField()
  room_type=models.CharField(max_length=100)
  room_number=models.IntegerField()