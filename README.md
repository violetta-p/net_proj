Данный проект представляет собой бэкенд-часть SPA веб-приложения.

Используемые технологии
Язык: python (версия интерпретатора python - 3.11.)
Фреймфорк: django (Django REST framework)
БД (СУБД) проекта: PostgreSQL
python
drf-yasg
cors
jwt (simple jwt)
Документация API
Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:

http://127.0.0.1:8000/redoc/ - ссылка на редок
http://127.0.0.1:8000/docs/ - ссылка на сваггер
CORS
Для безопасности API реализован CORS с помощью django-cors-headers.

В модуле settings.py необходимо внести изменения в следующие настройки, если у вас есть сторонние домены, обращающиеся к вашему API:

CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
Запуск проекта
Склонировать репозиторий в IDE: В терминале ввести команду: git clone https://github.com/violetta-p/net_proj

Установить виртуальное окружение и зависимости из файла requirements.txt:

Ввести следующие команды в терминале:

Создать виртуальное окружение: python3 -m venv venv
Активировать виртуальное окружение: venv\Scripts\activate.bat (Windows), source venv/bin/activate (Linux)
Установить зависимости: pip install -r requirements.txt
Создать файл .env по шаблону из файла .env.sample
Создать БД с названием, указанным в шаблоне (в пункте 4)

Создать таблицы в БД. Создать миграции: python manage.py makemigrations python manage.py migrate

Запустить сервер: python manage.py runserver


###Автор проекта: @Viit_115
