import redis

REDIS_CLIENT = redis.Redis(host="redis")


def only_one(function=None, timeout=60 * 1):
    """Enforce only one celery task at a time."""

    def _dec(run_func):
        """Decorator."""

        def _caller(*args, **kwargs):
            """Caller."""
            task, pk, target, time = args
            have_lock = False
            lock = REDIS_CLIENT.lock(target, timeout=timeout)
            try:
                have_lock = lock.acquire(blocking=False)
                if have_lock:
                    run_func(*args, **kwargs)
                else:
                    task.retry()
            finally:
                if have_lock:
                    lock.release()

        return _caller

    return _dec(function) if function is not None else _dec
