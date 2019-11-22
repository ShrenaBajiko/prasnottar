from django.contrib import admin
from . models import questions
from . models import profile
from . models import comment
from . models import tutor


admin.site.register(profile)
admin.site.register(questions)
admin.site.register(comment)
admin.site.register(tutor)


