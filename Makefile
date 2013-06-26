clean:
            @find . -name "*.pyc" -delete

deps:
            @pip install -r requirements.txt

setup: deps
            @python manage.py syncdb
            @python manage.py migrate
            @git remote add heroku git@heroku.com:pistalo.git

run:
            @python manage.py runserver 0.0.0.0:8000

remote_migrate:
            @heroku run python manage.py syncdb --noinput
            @heroku run python manage.py migrate

collectstatic:
            @heroku run python manage.py collectstatic --noinput

heroku:
            @git push heroku master

deploy: heroku remote_migrate collectstatic