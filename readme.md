# Required modules
Use pip or conda to install these packages!
- `django==4.0.6`
- `django_csv_exports==1.0.5`
- `django-import_export==2.8.0`
- `mssql-django==1.1.3`

# To run
`python manage.py runserver` - server should open at `http://127.0.0.1:8000/`
CTRL + C to stop server

LOGIN:
- user: esc
- pw: esc123456

add `/admin` to the end of server url in browser to access backend

# Making migrations
Any edits to the Models in `models.py` require you to run the following commands to save the changes:
- `python manage.py makemigrations`
- `python manage.py migrate`
