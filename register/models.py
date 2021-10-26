from django.db import models

# Create your models here.

class UserData(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    pro_image=models.ImageField(upload_to="profile/images",default="profile/images/default.png")
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=40)

class Friendslist(models.Model):
    user_id=models.IntegerField(default=-1)
    username=models.CharField(max_length=20)
    friend=models.CharField(max_length=20)
    friend_id=models.IntegerField(default=-1)
    
