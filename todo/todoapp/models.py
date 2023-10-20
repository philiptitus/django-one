from django.db import models
from django.conf import settings

# Create your models here.

class User_info(models.Model):

   user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   instagram = models.URLField(blank = True)
 


   def __str__(self):
      return self.user.username
   

class Tlist(models.Model):
   item = models.CharField(unique=True,max_length=250)

   def __str__(self):
         return self.item
   description = models.CharField(max_length=1000)

   def __str__(self):
      return self.description
   completion_date = models.DateField()
   
   def __str__(self):
      return str(self.completion_date) 
   