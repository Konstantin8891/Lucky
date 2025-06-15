from django.contrib import admin

from achievement.models import Achievement, AchievementUser


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(AchievementUser)
class AchievementUserAdmin(admin.ModelAdmin):
    pass
