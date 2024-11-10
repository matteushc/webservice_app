Include webservice app


# Install Django

1. pip install djangorestframework

2. pip install psycopg2-binary

3. Create diretory webservice_app and enter inside folder

4. django-admin startproject webservice_app . (if project exist not necessary)

5. django-admin startapp estabelecimento (if project exist not necessary)

6. python manage.py makemigrations

7. python manager.py migrate

8. python manage.py runserver

# Create Super User

* python manage.py createsuperuser
* caioabreu | padrão
* usuarioteste | usu123ar456

# Generate Token

```
python manage.py shell

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.all()
user.values() # See which user is admin and get id

user = user.get(id=1) # Example if user id is 2
token = Token.objects.create(user=user)
print(token.key)

```

Or

http post http://127.0.0.1:8000/api-token-auth/ username=admin password=123

# Starting Postgres container
sudo docker compose -f docker-compose.yml up