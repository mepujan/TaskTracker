from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('add', TaskCreateView.as_view(), name='add-task'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='update-task'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete-task')
]
