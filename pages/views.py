from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .models import ProjectGoal, Comment
from .forms import FeedbackForm, ProjectGoalForm, CommentForm

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
    comments = goal.comments.all()
    form = CommentForm()
    context = {
        'goal': goal,
        'comments': comments,
        'comment_form': form
    }
    return render(request, 'goal_detail.html', context)

@login_required
def add_comment(request, pk):
    goal = get_object_or_404(ProjectGoal, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.goal = goal
            comment.author = request.user
            comment.save()
            messages.success(request, 'Ваш комментарий добавлен!')
        else:
            messages.error(request, 'Ошибка при добавлении комментария.')
    return redirect('goal_detail', pk=pk)

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
            messages.success(request, 'Сообщение отправлено!')
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})

@login_required
def goal_create(request):
    if request.method == 'POST':
        form = ProjectGoalForm(request.POST, request.FILES)
        if form.is_valid():
            new_goal = form.save(commit=False)
            new_goal.author = request.user
            new_goal.save()
            form.save_m2m()
            messages.success(request, 'Задача создана!')
            return redirect('goal_detail', pk=new_goal.pk)
    else:
        form = ProjectGoalForm()
    return render(request, 'goal_form.html', {'form': form, 'title': 'Создание задачи'})

@login_required
def goal_update(request, pk):
    goal = get_object_or_404(ProjectGoal, pk=pk)
    if goal.author != request.user:
        return redirect('daily')
    if request.method == 'POST':
        form = ProjectGoalForm(request.POST, request.FILES, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача обновлена!')
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = ProjectGoalForm(instance=goal)
    return render(request, 'goal_form.html', {'form': form, 'title': 'Редактирование задачи'})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Регистрация прошла успешно!')
        return response