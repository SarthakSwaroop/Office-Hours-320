from django.db import models

# Create your models here.
class StudentAvailability(models.Model):
    email = models.EmailField()
    monday = models.CharField(max_length=50)
    tuesday = models.CharField(max_length=50)
    wednesday = models.CharField(max_length=50)
    thursday = models.CharField(max_length=50)
    friday = models.CharField(max_length=50)
    saturday = models.CharField(max_length=50)
    sunday = models.CharField(max_length=50)

class StudentSchedule(models.Model):
    email = models.EmailField()
    monday = models.CharField(max_length=50)
    tuesday = models.CharField(max_length=50)
    wednesday = models.CharField(max_length=50)
    thursday = models.CharField(max_length=50)
    friday = models.CharField(max_length=50)
    saturday = models.CharField(max_length=50)
    sunday = models.CharField(max_length=50)

class ProfessorOptions(models.Model):
    name = models.CharField(max_length=50)
    monday = models.CharField(max_length=50)
    tuesday = models.CharField(max_length=50)
    wednesday = models.CharField(max_length=50)
    thursday = models.CharField(max_length=50)
    friday = models.CharField(max_length=50)
    saturday = models.CharField(max_length=50)
    sunday = models.CharField(max_length=50)

class StudentRankings(models.Model):
    email = models.EmailField()
    first = models.CharField(max_length=50)
    second = models.CharField(max_length=50)
    third = models.CharField(max_length=50)

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    professor = models.BooleanField()