from django import forms
from api.models import TodoList

class Todoform(forms.ModelForm):
    class Meta:
        model=TodoList
        fields=['task_name','task_decription']
        widgets={
            'task_name': forms.TextInput(attrs={'placeholder': 'Enter Task', 'class': 'form-control', 'aria-label': 'Name'}),
            'task_decription': forms.Textarea(attrs={'placeholder': 'Enter Description', 'class': 'form-control', 'aria-label': 'Message'}),
            }