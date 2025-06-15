from django.contrib import admin
from django.contrib.auth.models import User

from chat.models import Chat, Message

admin.site.unregister(User)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name"]