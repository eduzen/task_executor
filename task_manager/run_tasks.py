
import time
import logging

from task_manager.jobs import jobs
from task_manager.task_config import task_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info(" Starting pooling...")
    start_time = time.time()
    while not jobs.empty():
        job_id, job_target, job_task_name = jobs.get()
        task_function = task_config[job_task_name]["func"]
        task_function.delay(job_id, job_target, start_time)
    logger.info(" All tasks added to the queue!")


if __name__ == "__main__":
    main()
