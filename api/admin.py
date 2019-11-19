from django.contrib import admin
from . models import questions
from . models import profile


admin.site.register(profile)
admin.site.register(questions)
