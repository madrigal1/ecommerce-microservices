# Ecommerce Backend using Flask,Django and Rabbit MQ

### Structure

There are three dockerised apps:

- the admin app which has the main database and is in django
-  the main backend written in flask which makes an internal call to the admin app \* the message queue using CloudAmqp, a free cloud RabbitMQ service
