from django.shortcuts import render, get_object_or_404, redirect
from .models import ProjectGoal
from .forms import FeedbackForm, ProjectGoalForm

def index(request):
    context = {
        'title': 'PROgress – главная страница',
        'welcome_text': 'Сервис для отслеживания игровых задач',
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

def contact_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(f"\n--- NEW FEEDBACK ---")
            print(f"Subject: {form.cleaned_data['subject']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text: {form.cleaned_data['text']}")
            print(f"--------------------\n")
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})

def goal_create(request):
    if request.method == 'POST':
        form = ProjectGoalForm(request.POST)
        if form.is_valid():
            new_goal = form.save()
            return redirect('goal_detail', pk=new_goal.pk)
    else:
        form = ProjectGoalForm()
    return render(request, 'goal_form.html', {'form': form, 'title': 'Создание задачи'})

def goal_update(request, pk):
    goal = get_object_or_404(ProjectGoal, pk=pk)
    if request.method == 'POST':
        form = ProjectGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = ProjectGoalForm(instance=goal)
    return render(request, 'goal_form.html', {'form': form, 'title': 'Редактирование задачи'})