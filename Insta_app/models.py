from django.db import models

# Create your models here.
class Profile(models.Model):
  profile_pic = models.ImageField(upload_to='profile/')
  bio = models.TextField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)

