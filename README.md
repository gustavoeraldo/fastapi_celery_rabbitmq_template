# Example of an API with: FastAPI, Celery and RabbitMQ

## Dependencies

For this particular project you must have installed in or machine:

- [Python](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu);
- [Pipenv](https://pipenv.pypa.io/en/latest/install/): `pip install pipenv`;
- [Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/).


## Setup

Clone the repository:
```bash
git clone https://github.com/gustavoeraldo/fastapi_celery_rabbitmq_template.git
```

Get into the project file: `cd rabbitmq_test`.
Once all [dependencies](##dependencies) are installed, 
activate the virtual environment:

```bash
pipenv shell
```

And than install all project dependencies: 
```bash
pipenv install
```

If you add any new library, remember to update the requirements with:
```bash
pipenv lock -r > requirements.txt
```

## RabbitMQ

You can set up rabbitmq by the following commands:
1. Pull the rabbitmq image, I recomend using the `rabbitmq:3-management` because
comes with a interface, so you easily interact with it.

```bash
docker pull rabbitmq:3-management
```

2. And finally, run the rabbitmq container:
```bash
docker run -d --hostname my-rabbit --name rabbit-ctn -p 8080:15672 -p 5672:5672 -p 25676:25676 rabbitmq:3-management
```

Now you can access the rabbitmq [interface](http://localhost:15672) locally:

```
http://localhost:15672
```

By default the credentials are: 
- username: guest
- password: guest

You can add new custom users and define their permissions ([first steps with rabboitmq](https://www.rabbitmq.com/access-control.html#basics)).

### Accessing the rabbitmq running container

Open the terminal and use:

```bash
# docker exec -it <container-name> bash 
docker exec -it rabbit-ctn bash
```

* Creating users in rabbitmq:

```bash
rabbitmqctl add_user myuser mypassword
```

```
rabbitmqctl add_vhost myvhost
```

```bash
rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
```

* Check queues command:

```bash
rabbitmqctl list_queues name messages messages_ready messages_unacknowledged
```

**RabbiMQ url access**: 

```.env
#                  protocol;//username:password@ip_address/virtual_host
export RABBIT_URL="amqp://guest:guest@localhost"
```
By default rabbitmq uses '/' as the virtual host, so in the example above
you don't need to specify unless another virtual host is desired.

Once you use docker-compose to run all the services on the same machine,
instead of using the IP address or host url, you can just use the container name.
So, you can have something like this:

```.env
export RABBIT_URL="amqp://guest:guest@rabbitmq_container_name/virtual_host"
```

To containers "see" eachother, **they have** to be in the **same network**.

## Celery

Once you have created the tasks and configured celery app in your project,
it is time to run celery workers.
Open another terminal tab and run the following command:

```
#         path.to.your.celery.app.config
celery -A app.v1.Config.celery_app worker --loglevel=INFO --autoscale=10,3 -n worker1@guest
```
Parameters explanation:
* `-A`: 
* `--loglevel` or `-l`: allows you to get the logs from workers;
* `--autoscale`: this allows to celery worker(s) use from 3 up to 10 threads when consuming one or more queues;
* `-n`: naming a worker.

There are many others parameters that can be used, so I suggest to get deeper in more details 
reading the documentation.

## What you can learn from this project 

- [X] Using lib [kombu]() to easily create different queue types and bind them into the celery app;
- [X] Management multiple databases with SQLAlchemy;
- [X] Using celery with rabbitmq as broker;
- [X] Saving tasks result into a database with SQLAlchemy 
    (by the way celery has a pre-defined table to save tasks result. 
    I don't know if there is a way to change this table schema, but you 
    can save some informations building a custom **on_save method**.);
- [X] Docker compose file with all services woring together.
- [X] Basic RabbitMQ and Celery usage.

## To DO

- [ ] Add retries policy;
- [ ] Add more custom configurations to celery app;
- [ ] Make a real cats/dogs identification.
- [ ] Test differents Databases:
    - [ ] MongoDB
    - [ ] Redis

Testing mermaid:

```mermaid
flowchart LR
    Start --> Stop
```

## References

* [Celery documentation](https://docs.celeryproject.org/en/stable/)
* [Celery good practices](https://betterprogramming.pub/python-celery-best-practices-ae182730bb81)
* [Kombu documentation](https://docs.celeryproject.org/projects/kombu/en/4.6.1/)
* [RabbitMQ documentation](https://www.rabbitmq.com/documentation.html)
* [Docker documentation](https://docs.docker.com/reference/)