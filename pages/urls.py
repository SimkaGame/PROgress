from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('daily/', views.daily, name='daily'),
    path('progress/', views.progress, name='progress'),
    path('game/', views.game, name='game'),
    path('goal/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('contact/', views.contact_view, name='contact'),
]