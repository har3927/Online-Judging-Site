from django.contrib import admin
from .models import Problem,TestCase,Solution
# Register your models here.
admin.site.register(Problem)
admin.site.register(Solution)
admin.site.register(TestCase)
