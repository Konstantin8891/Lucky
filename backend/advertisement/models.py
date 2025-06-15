from django.contrib.auth.models import User
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
        state = self._state.adding
        super().save(*args)
        if state:
            users = User.objects.all()
            for user in users:
                chat = Chat.objects.filter(user=user).first()
                if not chat:
                    chat = Chat.objects.create(user=user)
                    Message.objects.create(event=Message.EventType.advertisement, title=self.title, chat=chat)
