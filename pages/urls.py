from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('daily/', views.daily, name='daily'),
    path('progress/', views.progress, name='progress'),
    path('game/', views.game, name='game'),
    path('contact/', views.contact_view, name='contact'),
    path('goal/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('goal/add/', views.goal_create, name='goal_create'),
    path('goal/<int:pk>/edit/', views.goal_update, name='goal_update'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('goal/<int:pk>/comment/', views.add_comment, name='add_comment'),
]