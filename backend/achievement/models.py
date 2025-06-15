from django.contrib.auth.models import User
from django.db import models

from backend.mixins import TimeStampMixin
from chat.models import Chat, Message


class Achievement(TimeStampMixin):
    title = models.CharField(max_length=200)
    conditions = models.TextField()
    icon = models.ImageField(upload_to="static/achievements")
    user = models.ManyToManyField(User, related_name="achievements", through="AchievementUser")


class AchievementUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

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
            chat = Chat.objects.filter(user=self.user).first()
            if not chat:
                chat = Chat.objects.create(user=self.user)
            Message.objects.create(event=Message.EventType.achievement, title=self.achievement.title, chat=chat)
