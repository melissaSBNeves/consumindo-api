from django.db import models
from django.contrib.auth.models import User

class Holiday(models.Model):
   id = models.IntegerField(primary_key=True),
   name= models.CharField(max_length=255, null=False, blank=False, default='')
   date = models.DateField(null=False, blank=False,default='')
   type = models.CharField(max_length=80,null=False, blank=False,default='')
   user = models.ForeignKey(User, on_delete=models.CASCADE, default='')