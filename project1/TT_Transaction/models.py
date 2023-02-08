from django.db import models
from accounts.models import User
from Class_Schedule.models import Class_Schedule
from C_CD_S.models import C_CD_S
from Room.models import Room
#
# Create your models here.


class TT_Transaction(models.Model):
   user_id=models.ForeignKey(User, on_delete=models.CASCADE)
   #cs_id=models.IntegerField()#ForeignKey
   cs_id=models.ForeignKey(Class_Schedule,null=True,on_delete=models.CASCADE)
   #c_cd_s_id=models.IntegerField()#ForeignKey
   c_cd_s_id=models.ForeignKey(C_CD_S,null=True,on_delete=models.CASCADE)
   #room_id=models.IntegerField()#ForeignKey
   room_id=models.ForeignKey(Room,null=True,on_delete=models.CASCADE)
    
