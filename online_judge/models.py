from django.db import models

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
class Users(models.Model):
    user_name=models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    score = models.IntegerField(default = 0)
    rank=models.IntegerField(default=0)
    submissions = models.IntegerField(default=0)
#table 2
class Problems(models.Model):
    statement = models.CharField(max_length=1500)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=1200)
    difficulty = models.CharField(max_length=10)
    def __str__(self):
        return self.name
#table 3
class Solutions(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.CharField(max_length = 10,choices=Languages)
    verdict = models.CharField(max_length=20,choices=Verdicts)
    submitted_at = models.DateTimeField('Submitted On')
    def was_published_recently(self):
        return (self.submitted_at>=timezone.now()- datetime.timedelta(days=1))

#table 4
class TestCases(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    def __str__(self):
        return "test case {} for problem {}".format(self.pk, self.name)
