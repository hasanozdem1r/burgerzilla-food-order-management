poetry shell
flask db init
timeout 2
flask db migrate
timeout 2
flask db upgrade
