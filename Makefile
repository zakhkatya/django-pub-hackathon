COMPOSE := docker compose
WEB := web

.PHONY: help build up down restart logs ps shell dbshell migrate makemigrations superuser collectstatic test clean

help:
	@echo "Available commands:"
	@echo "  make build         - Build all containers"
	@echo "  make up            - Start containers in background"
	@echo "  make down          - Stop and remove containers"
	@echo "  make restart       - Restart containers"
	@echo "  make logs          - Follow logs"
	@echo "  make ps            - Show containers status"
	@echo "  make shell         - Open shell in web container"
	@echo "  make dbshell       - Open PostgreSQL shell"
	@echo "  make migrate       - Apply Django migrations"
	@echo "  make makemigrations- Create Django migrations"
	@echo "  make superuser     - Create Django superuser"
	@echo "  make collectstatic - Collect static files"
	@echo "  make test          - Run Django tests"
	@echo "  make clean         - Stop containers and remove volumes"

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

restart: down up

logs:
	$(COMPOSE) logs -f

ps:
	$(COMPOSE) ps

shell:
	$(COMPOSE) exec $(WEB) sh

dbshell:
	$(COMPOSE) exec db psql -U django_user -d django_db

migrate:
	$(COMPOSE) exec $(WEB) python manage.py migrate

makemigrations:
	$(COMPOSE) exec $(WEB) python manage.py makemigrations

superuser:
	$(COMPOSE) exec $(WEB) python manage.py createsuperuser

collectstatic:
	$(COMPOSE) exec $(WEB) python manage.py collectstatic --noinput

test:
	$(COMPOSE) exec $(WEB) python manage.py test

clean:
	$(COMPOSE) down -v --remove-orphans
