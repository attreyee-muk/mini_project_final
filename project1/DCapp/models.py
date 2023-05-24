from django.db import models
from accounts.models import User
# Create your models here.
class input_values(models.Model):
    user_id=models.ForeignKey(User , on_delete=models.CASCADE)
    no_periods=models.IntegerField()
    no_days=models.IntegerField()
    tt_id=models.IntegerField()
    DCapp_id=models.AutoField(primary_key=True)
    
