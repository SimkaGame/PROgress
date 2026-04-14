from django import forms

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