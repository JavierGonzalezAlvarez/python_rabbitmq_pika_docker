#!/bin/bash

RABBIT = platform-rabbitmq

run:
	docker network create rabbitmq_network || true
	docker-compose up -d

stop:
	docker-compose stop

restart:
	$(MAKE) stop && $(MAKE) run

ssh-mq:
	docker exec -it ${RABBIT} bash

