from django.shortcuts import render

from .models import Profile, Skill, Experience, Project


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    return render(request, 'resume/home.html', {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
    })
