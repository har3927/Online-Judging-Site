from django.db import models

# Create your models here.
#table 1
class Users(models.Model):
    password = models.CharField(max_length=50)
    score = models.IntegerField(default = 0)
    submissions = models.IntegerField(default=0)
#table 2
class Problems(models.Model):
    statement = models.CharField(max_length=1500)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=1200)
    difficulty = models.CharField(max_length=10)
#table 3
class Solutions(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    language = models.CharField(max_length = 10)
    verdict = models.CharField(max_length=20)
    submitted_at = models.DateTimeField('Submitted On')
#table 4
class TestCases(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
