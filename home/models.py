from unicodedata import name
from django.db import models

class patient(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    mob=models.CharField(max_length=10)
    add=models.CharField(max_length=10)
    bp=models.CharField(max_length=10)
    case=models.CharField(max_length=50)
    weight=models.CharField(max_length=10)
    class Meta:
        db_table="patient"


class patient_history(models.Model):
    patient_id=models.IntegerField()
    doctor_id=models.IntegerField()
    password=models.CharField(max_length=50)
    doctor_name=models.CharField(max_length=50)
    report=models.CharField(max_length=100)
    test_done=models.CharField(max_length=100)
    prescription=models.CharField(max_length=500)
    medication=models.CharField(max_length=500)
    date=models.DateField()
    class Meta:
        db_table="patient_history"

class doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    mob=models.CharField(max_length=10)
    class Meta:
        db_table="doctor"

class admin(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    mob=models.CharField(max_length=15)
    class Meta:
        db_table="admin"

