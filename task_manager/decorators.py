import redis
import logging

logger = logging.getLogger(__name__)

REDIS_CLIENT = redis.Redis(host="redis")


def only_one_task_per_user(function=None, timeout=60 * 1):
    """
        We use redis as cache to enforce only one celery
        task per user at a time.
    """

    def _dec(run_func):
        """Decorator"""

        def _caller(*args, **kwargs):
            """Caller"""
            task, pk, target, _ = args
            have_lock = False
            lock = REDIS_CLIENT.lock(target, timeout=timeout)
            try:
                have_lock = lock.acquire(blocking=False)
                if have_lock:
                    run_func(*args, **kwargs)
                else:
                    logger.info(f"User {target} is busy. We will retry the task with id {pk}.")
                    task.retry()
            finally:
                if have_lock:
                    lock.release()

        return _caller

    return _dec(function) if function is not None else _dec
