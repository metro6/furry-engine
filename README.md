#furry_engine project
#To start project*:

```bash
git clone https://github.com/metro6/furry-engine.git
cd furry-engine
```
Make settings file for Database.
```bash
touch src/custom_settings/custom_settings.py
nano src/custom_settings/custom_settings.py
```
Copy these text, or add you configurations database and SMTP server:
```
#USE THIS CONFIGURATION BATABASE!!!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}
#END CONFIGURATION DATABASE

#YOUR SMTP SERVER CONFIG
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_login'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
#END CONFIGURATION SMTP SERVER

```

Save it and run project:
```bash
(sudo) make build
(sudo) make up
```

You may stop project:
```bash
(sudo) make down
```

After downloading, the project is available at "http://you_domain_or_ip:8001"

Project used:
- docker-compose
- nginx
- gunicorn
- django
- postgresql

*Optional 

You can run the project in a more familiar way.
```bash
(sudo) docker-compose build
(sudo) docker-compose up
```

And stop this
```bash
(sudo) docker-compose down
```