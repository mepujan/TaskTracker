from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

TASK_STATUS = (
    ('todo', 'TODO'),
    ('inprogress', 'inprogress'),
    ('completed', 'completed')
)


class Task(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=TASK_STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def clean(self) -> None:
        if self.due_date < datetime.now().date():
            raise ValidationError("Due Date should be today or future date.")
        return super().clean()

    # api -> get_all_tasks

    class Meta:
        ordering = ('-updated',)
