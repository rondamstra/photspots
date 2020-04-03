# photspots
The photography location database for photographers.

This project is built in Python on the Django Framework. Data is stored in a MySQL database.
For the map functionality we use Open Streetmaps.

If you want to contribute to this project, create a cnf folder in the photspots_project directory, and create file mysql.cnf with your local database settings.

# mysql.cnf

[client]

database = %DBNAME%

user = %USERNAME%

password =%PASSWORD%

host = localhost

port = 3307
