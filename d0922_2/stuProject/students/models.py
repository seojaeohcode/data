from django.db import models

# Create your models here.
class Student(models.Model):
    s_no = models.AutoField(primary_key=True)