heroku_upload:
	git add . --all
	git ci -m 'It just for upload to Heroku'
	git push heroku master
	heroku run python manage.py syncdb
	heroku run python manage.py migrate
	heroku run python manage.py collectstatic
	heroku open

migrate:
	python manage.py schemamigration question --auto
	python manage.py migrate                
