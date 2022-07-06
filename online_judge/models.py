from django.db import models

# Create your models here.

#table 1
class Problem(models.Model):
    statement = models.CharField(max_length=1200)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=1200)
    difficulty = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#table 2
class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length = 10)
    verdict = models.CharField(max_length=200)
    submitted_at = models.DateTimeField('date submitted')
    submitted_code = models.CharField(max_length=250)

    def __str__(self):
        return self.verdict

#table 3
class TestCase(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return self.input
