# Mealy
Main features: you can share pictures of your daily meals, which will displayed like a diary. Show it to your family members and help your mom deciding dinner menus!

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


## Migrations on google app engine
```
mysql.server stop
~/cloud_sql_proxy -instances=mealy-245003:asia-east1:mealy-instance=tcp:3306 &
python manage.py migrate
```

## used libraries
- CSS, JS: https://getbootstrap.com/, https://api.jquery.com/
- Fonts: https://fontawesome.com/icons/
