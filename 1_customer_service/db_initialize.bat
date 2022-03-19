poetry run flask db init
timeout 2
poetry run flask db migrate
timeout 2
poetry run flask db upgrade
