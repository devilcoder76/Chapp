from django.db import models

class messages(models.Model):
    sender=models.CharField(max_length=20)
    reciever=models.CharField(max_length=20)
    message=models.CharField(max_length=300)
    date_time=models.DateTimeField(auto_now_add=True)