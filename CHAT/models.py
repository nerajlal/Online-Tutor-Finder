from django.db import models
from datetime import datetime

class Chat(models.Model):
    sender=models.CharField(max_length=200,null=True)
    reciever=models.CharField(max_length=200,null=True)
    sendername=models.CharField(max_length=200,null=True)
    message=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(default=datetime.now,max_length=20)

