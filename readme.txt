

First you can unzip the file name awais_test.zip.

Then create virtual environment using python -m venv "name".

Activate your virtual environment using name/scripts/activate.

Now install requrite library on your virtual environment using command pip install -r requriments.txt.

If you use another database goto settings.py and setup configer your database else use 
command python manage.py makemigrations this will create database and table in database. 

Then use command python manage.py migrate this will load the data in database.

Crate admin/superuser to take the token you need it to access the api carte using 
command python manage.py createsuperuser  

For runserver use command python manage.py runserver or runserver 8080


