from __future__ import absolute_import
from celery import Celery

app = Celery(
    "task_manager",
    broker="amqp://admin:mypass@rabbit:5672",
    backend="rpc://",
    include=["task_manager.tasks"],
)
