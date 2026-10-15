from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
