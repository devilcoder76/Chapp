from django.db import models

# Create your models here.

class feed_image(models.Model):
    user_id=models.IntegerField(default=-1)
    username=models.CharField(max_length=20)
    image=models.ImageField(upload_to="newsfeed/images")
    caption=models.CharField(max_length=300)
    likes=models.IntegerField()
    comments=models.IntegerField()
    date_time=models.DateTimeField(auto_now_add=True)

class likes(models.Model):
    user_id=models.IntegerField(default=-1)
    username=models.CharField(max_length=20)
    liked_username=models.CharField(max_length=20)
    img_id=models.IntegerField(default=-1)
    date_time=models.DateTimeField(auto_now_add=True)

class comments(models.Model):
    user_id=models.IntegerField(default=-1)
    username=models.CharField(max_length=20)
    cmt_username=models.CharField(max_length=20)
    img_id=models.IntegerField(default=-1)
    comment=models.CharField(max_length=300)
    date_time=models.DateTimeField(auto_now_add=True)
