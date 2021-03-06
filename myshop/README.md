Install RabbbitMQ Server on Ubuntu

`sudo apt-get install rabbitmq-server`

Check if rabbitmq is up and running. Enable management console:

`sudo rabbitmq-plugins enable rabbitmq_management`

 Open rabbitmq server config
 
 `sudo vi /etc/rabbitmq/rabbitmq-env.conf`

and comment out

`NODE_IP_ADDRESS=127.0.0.1`

Install `pango`

* For Mac: `brew install pango`
* For Ubuntu: `sudo apt-get install -y libsdl-pango-dev`

Start RabbitMQ Server

`rabbitmq-server` or `sudo service rabbitmq-server start`

Start Celery service

`celery -A myshop worker -l info`

Or use the included services.sh:

`./services.sh`
