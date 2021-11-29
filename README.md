# Ecommerce Backend using Flask,Django and Rabbit MQ

### Structure

There are three dockerised apps,
_ the admin app which has the main database and is in django
_ the main backend written in flask which makes an internal call to the admin app \* the message queue using CloudAmqp, a free cloud RabbitMQ service
