from datetime import datetime
from django.db import models


# Create your models here.
class Student(models.Model):
    s_no = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100)
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0)
    s_grade = models.IntegerField(default=0)
    s_gender = models.CharField(max_length=30)
    s_date = models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.s_name