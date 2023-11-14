from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    # context_object_name = 'tasks'
    template_name = 'task-list.html'
    paginate_by = 10


class TaskCreateView(CreateView):
    form_class = TaskForm
    model = Task
    context_object_name = 'form'
    success_url = reverse_lazy('task-list')
    template_name = 'create-task.html'


class TaskUpdateView(UpdateView):
    form_class = TaskForm
    model = Task
    context_object_name = 'form'
    success_url = reverse_lazy('task-list')
    template_name = 'update-task.html'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'confirm_delete.html'
