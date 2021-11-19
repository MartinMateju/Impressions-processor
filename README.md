update mysql.user set host = ‘%’ where user=’root’;

docker exec -it seznam-test-db-1   bash

mysql -u root -p

docker run --name=seznam-test-db-1 -p3306:3306 -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=seznam123 -d mysql/mysql-server:8.0.20

docker run --name mk-phpmyadmin -v phpmyadmin-volume:/etc/phpmyadmin/config.user.inc.php --link seznam-test-db-1:db -p :80 -d phpmyadmin/phpmyadmin


docker-compose build --no-cache


docker-compose -f stack.yml up


docker-compose down 


FLASK_APP=app.py FLASK_ENV=development flask run


docker run --name mk-phpmyadmin -v phpmyadmin-volume:/etc/phpmyadmin/config.user.inc.php --link mk-mysql:db -p 82:80 -d phpmyadmin/phpmyadmin


docker run --name mk-phpmyadmin -v phpmyadmin-volume:/etc/phpmyadmin/config.user.inc.php --link mk-mysql:db -p 82:80 -d phpmyadmin/phpmyadmin


SET PASSWORD FOR 'test2'@'localhost' = PASSWORD('mysecretcleartextpassword')

mysql -u root -p

mysql --host=127.0.0.1 --port=32000 -u root -p

CREATE DATABASE MYSQLTEST;


Volumes on MAC - https://stackoverflow.com/questions/38532483/where-is-var-lib-docker-on-mac-os-x

Docker flask mysql = setup https://stavshamir.github.io/python/dockerizing-a-flask-mysql-app-with-docker-compose/


python3 -m venv env 