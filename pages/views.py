from django.shortcuts import render

def index(request):
    context = {
        'title': 'PROgress – главная страница',
        'welcome_text': 'Сервис для отслеживания задач и личного развития',
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def daily(request):
    return render(request, 'pages/daily.html')

def progress(request):
    return render(request, 'pages/progress.html')

def game(request):
    return render(request, 'pages/game.html')