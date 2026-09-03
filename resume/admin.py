from django.contrib import admin

from .models import Profile, Skill, Experience, Education, Project, Metric, Language

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Metric)
admin.site.register(Language)
