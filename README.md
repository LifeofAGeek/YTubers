# YTubers

##Installations 

+ Install Python (if linux then pre-installed - check version using : python3 --version)
+ Add virtual environment : pipenv 2020 : pip3 install pipenv
+ Move into project folder and open terminal and type following commands :
+ pipenv shell - creates shell for your python virtual environment
+ pipenv install Pillow - image handling for django
+ pipenv install Django - Django framework
+ django-admin startproject tubers  
+ Test your installation using
+ + cd tubers 
+ + python3 manage.py runserver 
+ Install Postgresql and Postgres Admin 4:
+ + sudo apt-get install postgresql-12
+ + Follow line by line: https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu/ 


##Deploying Static files

+ COLLECTSTATIC
+ STATIC_ROOT
+ STATIC_URL
+ python3 manage.py startapp webpages 
+ Manage urls.py
+ Add webpages.apps.WebpagesConfig in Installed Apps in setting.py
