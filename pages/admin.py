from django.contrib import admin
from .models import ProjectGoal
from .models import ProjectGoal, Tag

admin.site.register(ProjectGoal)
admin.site.register(Tag)