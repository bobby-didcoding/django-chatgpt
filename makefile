ifneq (,$(wildcard ./.env))
	include .env 
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose up -d --build --remove-orphans

up:
	docker-compose up 

down:
	docker-compose down

down_v:
	docker-compose down -v

logs:
	docker-compose logs

app_logs:
	docker-compose logs app

db_logs:
	docker-compose logs db

migrate:
	docker-compose exec app python manage.py migrate --noinput

makemigrations:
	docker-compose exec app python manage.py makemigrations

shell:
	docker-compose exec app python manage.py shell

superuser:
	docker-compose exec app python manage.py createsuperuser

test:
	docker-compose exec app python manage.py test

prune:
	docker system prune

enter_app:
	docker exec -it demo_app bash
