# api_yamdb
api_yamdb

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Категории могут быть добавлены или изменены.

Команда разработчиков:
https://github.com/lerapraga тимлид и разработчик 1
https://github.com/Polya13 разработчик 2
https://github.com/ValeriyKolchanov разработчик 3

Запуск python3 -m venv env
Окружение source env/bin/activate
Апгрейднуть пип python3 -m pip install --upgrade pip
Зависимости pip install -r requirements.txt
Миграции python manage.py migrate --run-syncdb
Заполяем базу тестовыми данными (по желанию) python manage.py load_data
Создаем суперюзера (в админке меняем роль с юзера на админа) python manage.py createsuperuser
Запускаем проект python manage.py runserver

Полная документация к API находится по эндпоинту /redoc