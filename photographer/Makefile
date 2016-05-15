clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run: clean
	python manage.py runserver

migrate: clean
	python manage.py migrate

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

migrations: clean
	python manage.py makemigrations

user:
	python manage.py createsuperuser
