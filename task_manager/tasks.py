import time
from task_manager.celeryapp import app
from task_manager.decorators import only_one_task_per_user

drink_rate_limit = "5/s"
smoke_rate_limit = "3/s"
go_to_rate_limit = "2/s"


def get_time_since_start(start_time):
    return round(time.time() - start_time, 2)


@app.task(bind=True, rate_limit=drink_rate_limit, default_retry_delay=0.4)
@only_one_task_per_user()
def drink_beer(self, id, target, start_time):
    time.sleep(0.3)
    current_time = get_time_since_start(start_time)
    # burp
    print(f"{current_time} (ID {id}) {target}: beer")


@app.task(bind=True, rate_limit=smoke_rate_limit, default_retry_delay=0.4)
@only_one_task_per_user()
def smoke_cigarette(self, id, target, start_time):
    time.sleep(0.3)
    current_time = get_time_since_start(start_time)
    # puff
    print(f"{current_time} (ID {id}) {target}: cigarette")


@app.task(bind=True, rate_limit=go_to_rate_limit, default_retry_delay=0.4)
@only_one_task_per_user()
def go_to_toilet(self, id, target, start_time):
    time.sleep(0.3)
    current_time = get_time_since_start(start_time)
    # wizz
    print(f"{current_time} (ID {id}) {target}: toilet")
