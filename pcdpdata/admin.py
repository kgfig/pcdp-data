from django.contrib import admin
from pcdpdata.models import Assessment, Choice, Project, Question, User

# Register your models here.
admin.site.register(Project)
admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
