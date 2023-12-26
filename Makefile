start-server:
	. venv/bin/activate
	python manage.py runserver

db-backup:
	pg_dump -U postgres -h localhost -d postgres > reserve_dump.sql

db-load-backup:
	psql -U postgres -h localhost -d postgres > reserve_dump.sql
