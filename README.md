# task_executor [![Build Status](https://travis-ci.org/eduzen/task_executor.svg?branch=master)](https://travis-ci.org/eduzen/task_executor) [![codecov](https://codecov.io/gh/eduzen/task_executor/branch/master/graph/badge.svg)](https://codecov.io/gh/eduzen/task_executor)

For this exercise, we choose [Celery](http://www.celeryproject.org/) that is an asynchronous
task queue/job queue based on distributed message passing. Tasks can execute asynchronously
(in the background) or synchronously (wait until ready). Celery requires a message transport
to send and receive message. We choose [Rabbitmq](https://www.rabbitmq.com/) because sworks well celery.
Other broker could be [Redis](https://redis.io/), but for this exercise we use it as a memcachedb a
kind of persistent key-value store, for managing locks through all the tasks. We can use this
distributed lock to have our tasks try to acquire a non-blocking lock, and exit if the lock isn’t acquired.

## Installation
This project runs with `docker` (you can use traditional `virtualenv` but it's prepared out of the box for `docker`).
We choose `python 3.6.4` and not `python 3.7` because `Celery` doesn't support it yet.
Also to manage docker, we are using [docker-compose](https://docs.docker.com/compose/).

## Usage

If you already have `docker` and `docker-compose`, just run:

```bash
make start

# only test and flake8
make test
```
This command will download the images and build them in a container.


## Workers

Right now the celery worker is configure to execute __1) no more than 3 tasks in parallel__.
We can change this changing the number of concurrency of the worker:

```bash
celery worker --app=task_manager.celeryapp:app --concurrency=3 --loglevel=info
```

Other option is to run several workers:

```bash
docker-compose scale worker=5
```

## Tasks

Celery tasks have a custom decorator in order to achieve: __2) each target (dave for example) can only execute one task at once__.
To do this, we choose Redis instead of django cache though this last option is recommended [here][http://docs.celeryproject.org/en/latest/tutorials/task-cookbook.html#ensuring-a-task-is-only-executed-one-at-a-time]
because if memcached (or some other non- persistent cache) is used and (1) the cache daemon crashes or
(2) the cache key is culled before the appropriate expiration time / lock release,
then you have a race condition where two or more tasks could simultaneously acquire the task lock (see
[this](http://loose-bits.com/2010/10/distributed-task-locking-in-celery.html))

So, in case that the target is busy (locked), we will retry the task with a custom delay.
Also the task has a rate limit configured.

