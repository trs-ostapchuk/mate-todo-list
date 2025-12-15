from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        if task_id:
            task = get_object_or_404(Task, id=task_id)
            task.is_done = not task.is_done
            task.save()
        return redirect("todo_list:task-list")


class TaskFormView(generic.CreateView, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("todo_list:task-list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        if pk:
            return get_object_or_404(Task, pk=pk)
        return None


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list:task-list")


class ToggleCompleteView(generic.View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tags/tag_list.html"
    context_object_name = "tags"


class TagFormView(generic.CreateView, generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tags/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        if pk:
            return get_object_or_404(Tag, pk=pk)
        return None


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tags/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")

