# api_yamdb

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Категории могут быть добавлены или изменены.
## Разработчики

https://github.com/lerapraga тимлид и разработчик 1

https://github.com/Polya13 разработчик 2

https://github.com/ValeriyKolchanov разработчик 3


## Запуск в dev

Создаем окружение

```bash
  python3 -m venv env
```

Активируем окружение

```bash
  source env/bin/activate
```
Апгрейднуть пип

```bash
  python3 -m pip install --upgrade pip
```
Зависимости

```bash
  pip install -r requirements.txt
```
Миграции

```bash
  python manage.py migrate --run-syncdb
```
Заполяем базу тестовыми данными (по желанию) 

```bash
  python manage.py load_data
```
Создаем суперюзера (в админке меняем роль с юзера на админа)

```bash
  python manage.py createsuperuser
```
Запускаем проект

```bash
  python manage.py runserver
```
## API Reference

#### Полная документация к API находится по эндпоинту /redoc

