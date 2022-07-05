from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#choices
Languages = (
    ('py', 'Python'),
    ('cpp', 'C++'),
    ('c', 'C Language'),
    ('java', 'Java'),
)

Verdicts = (
    ('ACC', 'Accepted'),
    ('TLE', 'Time Limit Exceeded'),
    ('WA', 'Wrong Answer'),
    ('MLE', 'Memory Limit Exceeded'),
)

# Create your models here.

#table 1
class Problem(models.Model):
    statement = models.CharField(max_length=1500)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=1200)
    difficulty = models.CharField(max_length=10)
    def __str__(self):
        return self.name
#table 2
class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length = 10,choices=Languages)
    verdict = models.CharField(max_length=20,choices=Verdicts)
    submitted_at = models.DateTimeField('Submitted On')
    def __str__(self):
        return self.verdict

#table 3
class TestCase(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    def __str__(self):
        return "test case {} for problem {}".format(self.pk, self.name)
