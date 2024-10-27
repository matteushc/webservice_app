Include webservice app


# Install Django

1. pip install djangorestframework

2. Create diretory webservice_app and enter inside folder

3. django-admin startproject webservice_app . (if project exist not necessary)

4. django-admin startapp estabelecimento (if project exist not necessary)

5. python manage.py makemigrations

6. python manager.py migrate

7. python manage.py runserver

# Create Super User

* python manage.py createsuperuser

# Generate Token

```
python manage.py shell

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.all()
user.values() # See which user is admin and get id

user = user.get(id=2) # Example if user id is 2
token = Token.objects.create(user=user)
print(token.key)

```

Or

http post http://127.0.0.1:8000/api-token-auth/ username=admin password=123