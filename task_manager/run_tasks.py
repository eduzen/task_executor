
from __future__ import absolute_import
import time
from task_manager.jobs import jobs
from task_manager.task_config import task_config


def main():
    print("Starting pooling")
    while not jobs.empty():
        job_id, job_target, job_task_name = jobs.get()
        task_function = task_config[job_task_name]["func"]
        rate_limit = task_config[job_task_name]["rate_limit"]
        result = task_function.delay(job_id, job_target, time.time())
    print("done!")


if __name__ == "__main__":
    main()
