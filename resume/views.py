from django.shortcuts import render

from .models import Profile, Skill, Experience, Education, Project, Metric, Language


def home(request):
    return render(request, 'resume/home.html', {
        'profile': Profile.objects.first(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'education_higher': Education.objects.filter(kind=Education.KIND_HIGHER),
        'education_courses': Education.objects.filter(kind=Education.KIND_COURSE),
        'projects': Project.objects.all(),
        'metrics': Metric.objects.all(),
        'languages': Language.objects.all(),
    })
