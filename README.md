# Лента

Python 3.13

## Клонирование

https://github.com/Konstantin8891/Lucky.git

## Запуск проекта 

docker compose up --build

## Миграции

docker compose exec backend python manage.py migrate

## Создание ачивок

docker compose exec backend python manage.py add_achievements

## Создание пользователей

docker compose exec backend python manage.py add_users

## Создание суперпользователя

docker compose exec backend python manage.py createsuperuser

## Экспорт зависимостей

uv pip compile pyproject.toml --quiet --output-file backend/requirements.txt

## Запрос ленты

GET http://localhost:8000/api/v1/chat/messages/?user_id=1&search=&event=