python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

----

docker pull redis
docker run -d -p 6379:6379 -i -t redis:latest
redis-cli