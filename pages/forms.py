from django import forms
from .models import ProjectGoal

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        label='Тема письма',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

class ProjectGoalForm(forms.ModelForm):
    class Meta:
        model = ProjectGoal
        fields = ['name', 'description', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
        }