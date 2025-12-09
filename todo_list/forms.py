from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "tags": forms.SelectMultiple(attrs={"class": "form-select"}),
            "is_done": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }
