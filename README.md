# birth-pro
Birthday project

## Requirements
Remember to call these commands when you first initialize this app.
```
workon env1
brew install mysql
pip install mysqlclient=1.3.13
```

### Also setting up mysql is needed to connect your database.
```
workon env1
mysql.server start
mysql -uroot
mysql> create table birth
mysql> use mysql
mysql> create user birth@localhost identified with mysql_native_password by ''
mysql> grant all on birth.* to birth@localhost
mysql> quit
python manage.py migrate
```

## How to start
```
cd ~/birth-pro
workon env1
python manage.py runserver
```

Open http://localhost:8000 to see the app working!
http://localhost:8000/polls for the test app.
