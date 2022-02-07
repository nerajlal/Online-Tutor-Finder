from django.db import models
from datetime import datetime



class Users(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.IntegerField()
    password=models.CharField(max_length=200)
    account_choices=[('Teacher','Teacher'),('Parent','Parent')]
    account=models.CharField(max_length=10,null=True,choices=account_choices)
    gender_choices=[('Male','Male'),('Female','Female')]
    gender=models.CharField(max_length=10,null=True,choices=gender_choices)
    

    def __str__(self):
        return self.email
class Tutioninfo(models.Model):
    email=models.CharField(max_length=200,null=True)
    medium=models.CharField(max_length=200,null=True)
    subjects=models.CharField(max_length=200,null=True)
    cls=models.CharField(max_length=200,null=True)
    salary=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)

class Studentdata(models.Model):
    proimg=models.ImageField(upload_to="STATIC\images",null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.IntegerField()
    gender_choices=[('Male','Male'),('Female','Female')]
    gender=models.CharField(max_length=10,null=True,choices=gender_choices)
    address=models.CharField(max_length=500,null=True)
    institute=models.CharField(max_length=200,null=True)
    deadline=models.CharField(max_length=10,null=True)

    medium=models.CharField(max_length=200,null=True) 
    subjects=models.CharField(max_length=200,null=True)
    cls=models.CharField(max_length=200,null=True)
    salary=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(default=datetime.now)

class AppliedList(models.Model):
    student=models.CharField(max_length=200,null=True) 
    appliedby=models.CharField(max_length=200,null=True)
    appliedname=models.CharField(max_length=200,null=True)

class ForApproval(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.IntegerField()
    password=models.CharField(max_length=200)
    account_choices=[('Teacher','Teacher'),('Parent','Parent')]
    account=models.CharField(max_length=10,null=True,choices=account_choices)
    tutorimg=models.ImageField(upload_to="STATIC\images")
    
    gender_choices=[('Male','Male'),('Female','Female')]
    gender=models.CharField(max_length=10,null=True,choices=gender_choices)
    address=models.CharField(max_length=500,null=True)
    institute=models.CharField(max_length=200,null=True)

    medium=models.CharField(max_length=200,null=True) 
    subjects=models.CharField(max_length=200,null=True)

    cls=models.CharField(max_length=200,null=True)
    salary=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    certificate1=models.ImageField(upload_to="STATIC\images")
    certificate2=models.ImageField(upload_to="STATIC\images",null=True)
    

class Tutordata(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.IntegerField()
    account_choices=[('Teacher','Teacher'),('Parent','Parent')]
    account=models.CharField(max_length=10,null=True,choices=account_choices)
    tutorimg=models.ImageField(upload_to="STATIC\images")
    
    gender_choices=[('Male','Male'),('Female','Female')]
    gender=models.CharField(max_length=10,null=True,choices=gender_choices)
    address=models.CharField(max_length=500,null=True)
    institute=models.CharField(max_length=200,null=True)

    medium=models.CharField(max_length=200,null=True) 
    subjects=models.CharField(max_length=200,null=True)

    cls=models.CharField(max_length=200,null=True)
    salary=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    certificate1=models.ImageField(upload_to="STATIC\images")
    certificate2=models.ImageField(upload_to="STATIC\images")


class ConfirmedList(models.Model):
    teacher=models.CharField(max_length=200,null=True) 
    appliedby=models.CharField(max_length=200,null=True)
    appliedname=models.CharField(max_length=200,null=True)


