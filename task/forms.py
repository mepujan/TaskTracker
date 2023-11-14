from typing import Any
from django.forms import ModelForm
from .models import Task
from datetime import datetime, timedelta


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
