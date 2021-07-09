from django.db import models


# Create your models here.

class Candidate(models.Model):
    seq = models.AutoField(primary_key=True)
    c_no = models.IntegerField(null=False)
    c_grade = models.IntegerField(null=False)
    c_class = models.CharField(max_length=20)
    c_name = models.CharField(max_length=20)


class Student(models.Model):
    s_no = models.AutoField(primary_key=True)
    s_grade = models.IntegerField(null=False)
    s_class = models.CharField(max_length=20)
    s_birth = models.CharField(max_length=6)
    s_name = models.CharField(max_length=20)


class Vote(models.Model):
    s_no = models.ForeignKey('Student', on_delete=models.CASCADE)
    c_no = models.ForeignKey('Candidate', on_delete=models.CASCADE)
