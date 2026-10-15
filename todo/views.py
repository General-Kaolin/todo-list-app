from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task, Tag
from .forms import TaskForm, TagForm


# Task Views
class TaskListView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


class TaskToggleStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo:task-list")


# Tag Views
class TagListView(ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")
