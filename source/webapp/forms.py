from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]

class NoteForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Название')
    description = forms.CharField(max_length=500, required=True, label='Описание')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')
    todo_at = forms.DateTimeField(required=False, label='Время завершения задачи',
                                     input_formats=['%Y-%m-%d'],
                                     widget=forms.DateInput(attrs={'type': 'date'}
                                                            )
                                     )