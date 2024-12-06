## Installation

1. Клонируйте репозиторий:
```bash
git clone https://github.com/codingoleg/ksitest.git
```

2. Перейдите в папку проекта:
```bash
cd ./ksitest/
```
DUMP_SQL находится в ./drfsite/drfsite/settings.py. 
- Если DUMP_SQL True, то в консоли будут отображаться логи SQL-запросов вместе с временем его выполнения. 
Работает только при DEBUG = True

3. Настройте конфигурацию БД в ./drfsite/.env. Примените миграции:
```bash
python ./drfsite/manage.py makemigrations
python ./drfsite/manage.py migrate
```

4. Запустите проект:
```bash
python ./drfsite/manage.py runserver
```
## Эндпоинты:
- http://127.0.0.1:8000/v1/people/ [GET, POST] - просмотр всех записей или добавление новой
- http://127.0.0.1:8000/v1/people/<person_id> [GET] - получение информации о человеке
- http://127.0.0.1:8000/v1/people/<person_id> [PUT] - изменение информации о человеке
- http://127.0.0.1:8000/v1/people/<person_id>/ancestors [GET] - получение родословной