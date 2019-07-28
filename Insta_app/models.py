from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
  profile_pic = models.ImageField(upload_to='profile/')
  bio = models.TextField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)


class Image(models.Model):
    image = models.ImageField(upload_to = 'image/',)
    name = models.CharField(max_length=60)
    poster = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, related_name="images")
    # location = models.ForeignKey(Location, blank=True)
    
    # category = models.ForeignKey(Category,blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    comments= models.TextField(blank=True)

