# iShtagsBackend
#### Steps to run this project locally on windows:
- Requirements:
    1. Python 3.7 64x, download it form [here](https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe).
     
    2. MySQL server, MySQL workbench ...etc., download (mysql-installer-web-community-8.0.13.0.msi) form [here](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-web-community-8.0.13.0.msi).   
     
    3. MySQL-python interface for MYSQL database (mysqlclient‑1.3.13‑cp27‑cp27m‑win_amd64.whl) from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python).
    
    Notes: be sure that Python in SYSTEM ENVIRONMENT PATH.
    
    Recommendation: use Pycharm from jetbrains, download community edition form [here](https://www.jetbrains.com/pycharm/download/#section=windows).
    
- Follow this to run iShtagsBackend on your machine:
    1. clone the ripo:
        ```git clone https://github.com/zezo93/iShtagsBackend.git```
    2. install virtualenv globally ```pip install virtualenv```
    3. cd to iShtagsBackend ```cd iShtagsBackend```
    4. create and activate venv: 
        ```
        #create your venv
        virtualenv venv
          
        #activate your venv
        venv\Scripts\activate
        ```
    5. install requirements:
        ```pip install -r requirements.txt``` 
    6. install mysql-python ```pip install PATH_TO/mysqlclient‑1.3.13‑cp27‑cp27m‑win_amd64.whl```
    7. make a copy for you local environment by making a copy of `local.temp.py` and rename it to `local.py`,
    change local.py settings to configurations you made during MYSQL server installation. 
    Note: don't forget to create your database named `ishtags-dev` using workbench in your local connection.
    
    8. migrate database models using: `python manage.py migrate`.
    9. create superuser for admin: `python manage.py createsuperuser --email admin@ishatgs.com --username admin`, and create password for it.
    10. TADAAAA! now we can run our server:
        ```
        python manage.py runserver
        
        Performing system checks...
    
        System check identified no issues (0 silenced).
        October 28, 2018 - 01:53:06
        Django version 2.0.3, using settings 'settings.local'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK. 
        ```
    
    
    
    