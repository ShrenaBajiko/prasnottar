from django.contrib import admin
from . models import questions
from . models import profile
from . models import comment


admin.site.register(profile)
admin.site.register(questions)
admin.site.register(comment)

