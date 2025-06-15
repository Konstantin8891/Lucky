import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):

        users = {
            1: {"first_name": "Василий", "username": "Василий"},
            2: {"first_name": "Михаил", "username": "Михаил"},
            3: {"first_name": "Петр", "username": "Петр"},
            4: {"first_name": "Иван", "username": "Иван"},
            5: {"first_name": "Валентин", "username": "Валентин"},
            6: {"first_name": "Олег", "username": "Олег"},
            7: {"first_name": "Максим", "username": "Максим"},
            8: {"first_name": "Вениамин", "username": "Вениамин"},
            9: {"first_name": "Пафнутий", "username": "Пафнутий"},
            10: {"first_name": "Мирослав", "username": "Мирослав"},
        }
        random.seed(5)
        for i in range(3):
            _id = random.choice(list(users.keys()))
            User.objects.create(id=_id, **users[_id])
