from django.conf import settings
from django.db import models
from ulid import ULID


def generate_ulid():
    return str(ULID())


class Task(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=26,
        default=generate_ulid(),
        editable=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    notified = models.BooleanField(default=False)