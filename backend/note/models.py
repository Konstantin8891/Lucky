from django.contrib.auth.models import User
from django.db import models

from backend.mixins import TimeStampMixin
from chat.models import Chat, Message


class Note(TimeStampMixin):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE)

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        state = self._state.adding
        super().save()
        if state:
            chat = Chat.objects.filter(user=self.user).first()
            if not chat:
                chat = Chat.objects.create(user=self.user)
            Message.objects.create(event=Message.EventType.note, title=self.title, chat=chat)
