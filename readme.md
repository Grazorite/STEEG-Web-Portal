# Required modules
Use pip or conda to install these packages!
- `django`
- `django_csv_exports`

# To run
`python manage.py runserver` - server should open at `http://127.0.0.1:8000/`
CTRL + C to stop server

LOGIN:
- user: esc
- pw: esc123456

add `/admin` to the end of server url in browser to access backend

# Modifying database
ENSURE `db.sqlite3` is deleted first!!
any edits to the code need to run the following commands:
- `python manage.py makemigrations`
- `python manage.py migrate`

then create a superuser (login details in previous header) by `python manage.py createsuperuser`