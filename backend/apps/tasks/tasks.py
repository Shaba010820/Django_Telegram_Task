from celery import shared_task
from django.utils import timezone

from .models import Task
from .notifications import send_telegram_message


@shared_task
def notify_due_tasks():
    now = timezone.now()

    tasks = Task.objects.filter(
        due_date__lte=now,
        is_completed=False,
        notified=False,
    ).select_related("user")

    for task in tasks:
        send_telegram_message(
            telegram_id=task.user.telegram_id,
            text=f"⏰ Задача «{task.title}» просрочена",
        )

        task.notified = True
        task.save(update_fields=["notified"])