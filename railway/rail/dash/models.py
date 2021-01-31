
from django.db import models

# Create your models here.

class profile(models.Model):
    user=models.CharField(max_length=25,primary_key=True)
    passwd=models.CharField(max_length=25)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    dob=models.DateField()
    gender=models.CharField(max_length=25)
    phn=models.BigIntegerField()

class train(models.Model):
    tno=models.IntegerField(primary_key=True)
    tname=models.CharField(max_length=30)
    tstart=models.CharField(max_length=30)
    tend=models.CharField(max_length=30)
    t1AC=models.IntegerField()
    t2AC=models.IntegerField()
    t3AC=models.IntegerField()
    tsleep=models.IntegerField()

class ticket(models.Model):
    tid=models.BigIntegerField(primary_key=True)
    price=models.IntegerField()
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=30)
    departure=models.DateField(max_length=30)
    classtype=models.CharField(max_length=30)
    tname=models.CharField(max_length=30)
    pnr=models.BigIntegerField()
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=25)
    phn=models.BigIntegerField()
    status=models.BooleanField(max_length=10)
    creatorid=models.CharField(max_length=25)
