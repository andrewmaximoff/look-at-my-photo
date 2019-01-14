# [Look At My Photo](https://look-at-my-photo.herokuapp.com/)
Instagram clone, without JS(just jQuery and [Waypoints](http://imakewebthings.com/waypoints/) for Infinite Scroll).

For storage media files use django-storages(Dropbox). Look config/.env.template and settings.py.

Install requirements and activate virtualenv:
```bash
pipenv install
pipenv shell
```

Database migration:
```bash
python manage.py makemigrations
python manage.py migrate 
```

Run local server:
```bash
python manage.py runserver
```