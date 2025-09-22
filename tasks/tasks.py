from celery import shared_task
from .models import Task
from django.core.mail import send_mail

@shared_task
def send_task_reminders():
    tasks = Task.objects.filter(is_completed=False)
    for task in tasks:
        send_mail(
            subject=f"Reminder: {task.title}",
            message=task.description,
            from_email="noreply@todoapp.com",
            recipient_list=[task.user.email],
        )
