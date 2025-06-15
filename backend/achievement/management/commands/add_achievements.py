import random

from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand

from achievement.models import Achievement


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("sample.jpeg", "rb") as f:
            image = ImageFile(f)
            achievements = {
                1: {"title": "За успехи в работе", "conditions": "Более 10 лет работы в компании", "icon": image},
                2: {"title": "За поднятие сервера", "conditions": "За 5 секунд", "icon": image},
                3: {
                    "title": "За сомнительные достижения", "conditions": "Реализация регистрации за 2 месяца", "icon": image
                },
                4: {"title": "За прохождение киберпанка", "conditions": "В рабочее время", "icon": image},
                5: {"title": "Медаль 100 багов", "conditions": "За одну неделю", "icon": image},
                6: {"title": "Вам ещё повезёт", "conditions": "И проект запуститься, но это не точно", "icon": image},
                7: {"title": "Житель кофепоинта", "conditions": "За борьбу с кофейными зернами", "icon": image},
                8: {"title": "Скрытое знание", "conditions": "Унес все секреты проекта в могилу", "icon": image},
                9: {"title": "Исследователь ассемблера", "conditions": "И его применения в веб разработке", "icon": image},
                10: {"title": "Чужой среди своих", "conditions": "За слив базы конкурентам", "icon": image},
            }
            random.seed(1)
            for i in range(2):
                _id = random.choice(list(achievements.keys()))
                Achievement.objects.create(id=_id, **achievements[_id])
