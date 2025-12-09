from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:task-list")


class ToggleCompleteView(generic.View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("/")


# TAGS
class TagListView(generic.ListView):
    model = Tag
    template_name = "tags/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tags/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tags/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tags/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")
