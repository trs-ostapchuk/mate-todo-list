from django.urls import path
from .views import (
    TaskListView,
    TaskFormView,
    TaskDeleteView,
    ToggleCompleteView,
    TagListView,
    TagFormView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/add/", TaskFormView.as_view(), name="task-create"),
    path("task/<int:pk>/edit/", TaskFormView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", ToggleCompleteView.as_view(), name="task-toggle"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/", TagFormView.as_view(), name="tag-create"),
    path("tags/<int:pk>/edit/", TagFormView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"
