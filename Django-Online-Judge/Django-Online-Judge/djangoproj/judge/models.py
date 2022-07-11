from django.db import models

class Problem(models.Model):

    class Difficulty(models.TextChoices):
        easy = "EASY"
        medium = "MEDIUM"
        hard = "HARD"

    name = models.CharField(max_length=50)
    statement = models.TextField()
    code = models.CharField(max_length=10)
    difficulty = models.CharField(
        max_length=6,
        choices=Difficulty.choices,
        default=Difficulty.easy
    )

    def __str__(self):
        return self.name

class Solution(models.Model):

    class Verdict(models.TextChoices):
        Success = "SUCCESS"
        COMPILATION_ERROR = "COMPILATION_ERROR"
        Wrong_Output = "Wrong Output"
        Time_Limit_Exceeded = "TIME LIMIT EXCEEDED"
        Runtime_Error = "RUNTIME ERROR"

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(
        max_length=20,
        choices=Verdict.choices
    )
    submittedAt = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.problem.code + "_" + self.verdict

class TestCase(models.Model):
    input = models.TextField()
    output = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return "test_" + self.problem.code
