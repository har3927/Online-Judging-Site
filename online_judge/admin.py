from django.contrib import admin
from .models import Users,Problems,Solutions,TestCases
# Register your models here.
admin.site.register(Users)
admin.site.register(Problems)
admin.site.register(Solutions)
admin.site.register(TestCases)
