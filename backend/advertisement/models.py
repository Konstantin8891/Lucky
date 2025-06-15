from django.db import models

from backend.mixins import TimeStampMixin
from chat.models import Chat, Message


class Advertisement(TimeStampMixin):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="static/advertisement")
    link = models.URLField()

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        super().save()
        chats = Chat.objects.all()
        for chat in chats:
            Message.objects.create(event=Message.EventType.advertisement, title=self.title, chat=chat)
