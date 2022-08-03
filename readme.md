# Required modules
Use pip or conda to install these packages!
- `django==3.2.13`
- `django_csv_exports==1.0.5`
- `django-filter==22.1`
- `django-import_export==2.8.0`
- `mssql-django==1.1.3`

# To run
`python manage.py runserver` - server should open at `http://127.0.0.1:8000/`

CTRL + C to stop server

# Making migrations
Any edits to the Models in `models.py` require you to run the following commands to save the changes:
- `python manage.py makemigrations`
- `python manage.py migrate`
