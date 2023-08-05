# pika & rabbitmq

* $ docker network create rabbitmq-network

* $ make run
* $ make stop
* $ make ssh-mq

## create image
* $ docker build -t receiver .
* $ docker build -t sender .

## create container and run
* $ docker run -it --network rabbitmq_network receiver
* $ docker run -it --network rabbitmq_network sender

* $ docker container prune