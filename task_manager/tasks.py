from __future__ import absolute_import
import time
from task_manager.celeryapp import app
from task_manager.task_config import task_config

drink_rate_limit = task_config["drink_beer"]["rate_limit"]
smoke_rate_limit = task_config["smoke_cigarette"]["rate_limit"]
go_to_rate_limit = task_config["go_to_toilet"]["rate_limit"]


def getTimeSinceStart(start_time):
    return round(time.time() - start_time, 2)


@app.task(bind=True, task_time_limit=drink_rate_limit, default_retry_delay=10)
def drink_beer(self, id, target, start_time):
    time.sleep(0.3)
    current_time = getTimeSinceStart(start_time)
    # burp
    print(f"{current_time} (ID {id}) {target}: beer")


@app.task(bind=True, task_time_limit=smoke_rate_limit, default_retry_delay=10)
def smoke_cigarette(self, id, target, start_time):
    time.sleep(0.3)
    current_time = getTimeSinceStart(start_time)
    # puff
    print(f"{current_time} (ID {id}) {target}: cigarette")


@app.task(bind=True, task_time_limit=go_to_rate_limit, default_retry_delay=10)
def go_to_toilet(self, id, target, start_time):
    time.sleep(0.3)
    current_time = getTimeSinceStart(start_time)
    # wizz
    print(f"{current_time} (ID {id}) {target}: toilet")
