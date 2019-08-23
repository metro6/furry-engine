#furry_engine project
#Для старта проекта*:

```bash
git clone https://github.com/metro6/furry-engine.git
cd furry-engine
```
Создайте файл с настройками БД
```bash
touch src/custom_settings/custom_settings.py
nano src/custom_settings/custom_settings.py
```
Запишите файл с конфигурацией БД
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}
```

Сохраните это и запустите проект:
```bash
(sudo) make build
(sudo) make up
```

Остановить проект:
```bash
(sudo) make down
```

После окончания загрузки, проект запустится тут: http://localhost:8001"

В проекте используются:
- docker-compose
- nginx
- gunicorn
- django
- django-rest-framework
- postgresql

После запуска проекта, вы можете подключиться к докеру и создать суперпользователя (он понадобится для получения токена)
```bash
docker-compose exec web bash
```
После инклуда в докер, создаете пользователя:
```bash
./manage.py createsuperuser
```
Дальше, сделайте тестовые запросы, получите токен авторизации, и сделайте пару запросов. 
Подробная документация по API доступна по адресу http://localhost:8001/api/v1/swagger/