# "Newspaper agency"

Python Django project for managing the redactors responsible for each newspaper issue.

In this app you cat add, update, delete newspapers
and add, update, delete redactors for these newspapers.

https://newspaper-agency-v2x8.onrender.com/ - LIVE

username:

```shell
user.public
```
password:
```shell
Pdmp123Ps3
```

## Technologies

- Python 3
- Django 5
- SQL
- Bootstrap 5

## Installation

1. Install Python3:

```shell
www.python.org/
```

2. Install Git:

```shell
git-scm.com/
```

3. Clone the repository.

main branch:
```shell
git clone https://github.com/skyfoxwork/newspaper-agency.git
```

develop branch

```shell
git clone -b develop https://github.com/skyfoxwork/newspaper-agency.git
```

4. Navigate to the project directory:

```shell
cd newspaper-agency
```

5. Create virtual environment:

```shell
python3 -m venv venv
```

6. Activate virtual environment (venv).

MacOS, Linux:

```shell
source venv/bin/activate
```
   Windows:

```shell
venv\Scripts\activate
```


if you need to deactivate virtual environment use:

```shell
deactivate
```

7. Install dependencies:

```shell
pip install -r requirements.txt
```

8. Create database:

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

9. Fill database with data:

```shell
python3 manage.py loaddata newspaper_agency_fixture.json
```
10. Run project:

```shell
python3 manage.py runserver
```

11. Visit your web browser:

```shell
http://127.0.0.1:8000/ or localhost:8000
```
to log in:

```shell
username: user.public
password: Pdmp123Ps3
```

or you can create your superuser with:

```shell
python3 manage.py createsuperuser
```

and login as your custom superuser.
