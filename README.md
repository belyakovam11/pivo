# Пивоварня «Движение» на Django

## Запуск локально

```bash
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Откройте http://127.0.0.1:8000/. Для входа в административную панель создайте администратора командой `python3 manage.py createsuperuser`, затем откройте http://127.0.0.1:8000/admin/.

## Что сохраняется

Заявки частных и оптовых покупателей, записи на мероприятия и идеи для проекта сохраняются в SQLite и доступны в Django admin.

Для рабочего окружения установите `DJANGO_DEBUG=0`, задайте уникальный `DJANGO_SECRET_KEY` и перечислите разрешенные домены через `DJANGO_ALLOWED_HOSTS`.
