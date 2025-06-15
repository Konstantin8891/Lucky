from django.contrib.auth.models import User
from django.db import models

from backend.mixins import TimeStampMixin


class Chat(TimeStampMixin):
    user = models.ForeignKey(User, related_name="chat", on_delete=models.CASCADE)


class Message(TimeStampMixin):
    class EventType(models.TextChoices):
        note = "note"
        achievement = "achievement"
        advertisement = "advertisement"

    event = models.CharField(max_length=50, choices=EventType.choices)
    title = models.CharField(max_length=200)
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
