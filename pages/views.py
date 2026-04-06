from django.shortcuts import render
from .models import ProjectGoal
from django.shortcuts import render, get_object_or_404
from .models import ProjectGoal

def index(request):
    context = {
        'title': 'PROgress – главная страница',
        'welcome_text': 'Сервис для отслеживания  игровых задач',
    }
    return render(request, 'index.html', context)

def daily(request):
    goals = ProjectGoal.objects.all() 
    context = {
        'goals': goals,
    }
    return render(request, 'daily.html', context)

def goal_detail(request, pk):
    goal = get_object_or_404(ProjectGoal, pk=pk)
    
    context = {
        'goal': goal
    }
    return render(request, 'goal_detail.html', context)

def about(request):
    return render(request, 'about.html')

def progress(request):
    return render(request, 'progress.html')

def game(request):
    return render(request, 'game.html')