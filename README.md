# "Newspaper agency"

Project for managing the redactors responsible for each newspaper issue.

In this app you cat add, update, delete newspapers
and add, update, delete redactors for these newspapers.

## Technologies

- Python 3
- Django 5
- SQL
- Bootstrap 5

## Installation

Install Python3: https://www.python.org/

Install Git: https://git-scm.com/

Clone the repository:

   git clone https://github.com/skyfoxwork/newspaper-agency.git

   git clone -b develop https://github.com/skyfoxwork/newspaper-agency.git

1. Navigate to the project directory:

   cd newspaper-agency

2. Create virtual environment:

   python3 -m venv venv

3. Activate virtual environment (venv):
   MacOS, Linux:

   source venv/bin/activate

   (if you need for deactivating virtual environment use):
       deactivate

4. Install dependencies:

   pip install -r requirements.txt

5. Create database:

   python3 manage.py makemigrations

   python3 manage.py migrate

6. Optional, fill database with data:

   python3 manage.py loaddata newspaper_agency_fixture.json

7. Run project:

   python3 manage.py runserver

8. Visit your web browser:

   http://127.0.0.1:8000/ or localhost:8000

   use to log in:
   
   username: user.public
   password: Pdmp123Ps3

   or you can create your superuser with:

   python3 manage.py createsuperuser
