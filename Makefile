help:
	@echo "help  -- print this help"
	@echo "start -- start docker stack"
	@echo "stop  -- stop docker stack"
	@echo "ps    -- show status"
	@echo "clean -- clean all artifacts"
	@echo "dockershell -- bash shell inside of docker"
	@echo "test  -- run tests using docker"
	@echo "bootstrap --build containers, run django migrations, load fixtures and create the a superuser"

build:
	docker-compose build

start: clean
	docker-compose up --build

dockershell:
	docker-compose run --rm launch-task bash

run-tasks:
	docker-compose up --build launch-task

stop:
	docker-compose stop

ps:
	docker-compose ps

clean: stop
	docker-compose rm --force -v

only_test: build
	docker-compose run --rm launch-task pytest --cov=. --cov-config setup.cfg

pep8:
	docker-compose run --rm launch-task flake8 task_manager

test: build pep8 only_test


.PHONY: help start stop ps clean test dockershell shell_plus only_test pep8
