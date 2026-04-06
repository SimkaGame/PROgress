from django.shortcuts import render
from .models import ProjectGoal

def index(request):
    goals = ProjectGoal.objects.all()
    
    context = {
        'title': 'PROgress – главная страница',
        'welcome_text': 'Сервис для отслеживания задач и личного развития',
        'goals': goals,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def daily(request):
    return render(request, 'daily.html')

def progress(request):
    return render(request, 'progress.html')

def game(request):
    return render(request, 'game.html')